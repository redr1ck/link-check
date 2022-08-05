import asyncio
import aiohttp
from bs4 import BeautifulSoup

result = {}


async def fetch(url, page_number, session):
    async with session.get(url) as response:
        date = response.headers.get("DATE")
        print("{}:{}".format(date, response.url))
        page = await response.text()
        soup = BeautifulSoup(page, "html.parser")
        link = soup.find('a')
        h2 = soup.find('h2')
        if link is None:
            if h2 is None:
                result[f"Page-{page_number}"] = f"Link does not exist! URL: {response.url}"
                return
            else:
                print(h2.text)
                if h2.text == "\r\nЭто последняя страница на ней нет ссылки. Так надо.\r\n\r\n":
                    result[f"Page-{page_number}"] = f"Last page! URL: {response.url}"
                    return
        else:
            if link.text == "":
                result[f"Page-{page_number}"] = f"Link exists but not visible! URL: {response.url}"
                return
            if link.text != "Next" and link.text is not None:
                result[f"Page-{page_number}"] = f"Link name is different from 'Next'! URL: {response.url}"
                return


async def bound_fetch(sem, url, page_number, session):
    # Getter function with semaphore.
    async with sem:
        await fetch(url, page_number, session)


async def run(r):
    url = "https://s3.eu-central-1.amazonaws.com/qa-web-test-task/{}.html"
    tasks = []
    # create instance of Semaphore
    sem = asyncio.Semaphore(1000)
    connector = aiohttp.TCPConnector(ssl=False)

    # Create client session that will ensure we dont open new connection
    # per each request.
    async with aiohttp.ClientSession(connector=connector) as session:
        for i in range(1, r):
            # pass Semaphore and session to every GET request
            task = asyncio.ensure_future(bound_fetch(sem, url.format(i), i, session))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        await responses


number = 10000
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(number))
loop.run_until_complete(future)

# Save results in file
with open("result_aio.txt", "w") as file:
    for k, v in result.items():
        file.write(f"{k} : {v}\n")