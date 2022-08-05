import requests
import logging
import itertools
from bs4 import BeautifulSoup

result = {}


def fetch():
    for i in itertools.count(1, 1):
        logging.info(f"Getting page number {i} ...")
        print(f"Getting page number {i} ...")
        r = requests.get(f"https://s3.eu-central-1.amazonaws.com/qa-web-test-task/{i}.html")
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, "html.parser")
        link = soup.find('a')
        h2 = soup.find('h2')
        if r.status_code != 200:
            break
        if link is None:
            if h2 is None:
                result[f"Page-{i}"] = f"Link does not exist! URL: {r.url}"
                return
            else:
                print(h2.text)
                if h2.text == "\r\nЭто последняя страница на ней нет ссылки. Так надо.\r\n\r\n":
                    result[f"Page-{i}"] = f"Last page! URL: {r.url}"
                    return
        else:
            if link.text == "":
                result[f"Page-{i}"] = f"Link exists but not visible! URL: {r.url}"
                return
            if link.text != "Next" and link.text is not None:
                result[f"Page-{i}"] = f"Link name is different from 'Next'! URL: {r.url}"
                return


fetch()
print("Start saving results in file ...")

with open("result_req.txt", "w") as file:
    for k, v in result.items():
        file.write(f"{k} : {v}\n")

print("Saved successfully")
