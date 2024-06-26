## eng
# Description
The repository contains two script files aiohttp_script.py and link_req_script.py along with a dependencies file named requirements.txt. Interestingly, both scripts address the same task but employ different approaches.
### To run the tests:
1. Clone the repository.
2. Create and activate a virtual environment (venv):

      ```
      python3 -m venv venv

      # On Windows:
      venv\Scripts\activate

      # On macOS/Linux:
      source venv/bin/activate
      ```
3. Install dependencies: 

      `pip install -r requirements.txt`

4. Run scripts: 

      `python aiohttp_script.py` - This command is used to execute the script utilizing the aiohttp library. Upon successful completion, a file named _result_aio.txt_ containing the execution results will be generated in the current directory.

      `python link_req_script.py` - This command is used to execute the script utilizing the requests library. Upon successful completion, a file named _result_req.txt_ containing the execution results will be generated in the current directory.






## rus
# _Краткое описание_ 

В репозитории имеются файлы скриптов aiohttp_script.py и link_req_script.py, так же файл с зависимостями
requirements.txt

# _Как запустить скрипты_
Процесс подготовки к запуску скриптов состоит из четырех небольших последовательных шагов:
- установить Python
- склонировать репозиторий 
- запустить виртуальное окружение
- установить зависимости

### _1) установка python_
В этой части воспользуемся готовой инструкцией, например вот отсюда:
https://tutorial.djangogirls.org/ru/python_installation/

### _2) клонируем репозиторий_
Запускаем терминал (командную строку) из директории, в которую хотим склонировать репозиторий и выполняем 
вот эту команду:

`git clone https://github.com/redr1ck/link-check.git`

либо же просто скачать zip архив и распаковать в нужном вам месте

### _3) запускаем виртуальное окружение_
Для начала создаем виртуальное окружение. Для этого запускаем терминал из директории куда 
скачали код в прошлом шаге и выполняем в нем команду:

`python -m venv {env_name}`, где {env_name} - имя создаваемого окружения

после этого окружение можно запускать:

для Linux выполнить: `source ./.venv/bin/activate` 

для Windows: `.\venv\Scripts\Activate.ps1`

После активации предложение командной строки должно измениться: в нем появится имя 
каталога виртуального окружения в скобках

### _4) устанавливаем зависимости_
Все просто. В вируальном окружении выполняем команду:

`pip install -r requirements.txt`

### Теперь все готово для запуска скриптов. Сделать это можно выполнив команду:

`python aiohttp_script.py` - для запуска скрипта с aiohttp (после успешного завершения в 
директории появится файл с результатом выполнения _result_aio.txt_)

и `python link_req_script.py` для запуска скрипта с requests (после успешного завершения в 
директории появится файл с результатом выполнения _result_req.txt_)
