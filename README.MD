Для запуска бота необходимо:

1) В репозитории создать виртуальную среду env;

py -m venv env


2) Закачать нужные пакеты из requirements.txt;

pip install -r requirements.txt


3) Импортировать либо подключить секретную базу данных в постгрес;


4) Создать и настроить config.cfg по образцу;

[TOKEN]  
TOKEN  
[PASSWORD]  
PASSWORD  
[DB_HOST]  
DATABAZE_HOST  
[DB_USER]  
DATABAZE_USER  
[DB_PASSWORD]  
DATABAZE_PASSWORD  
[DB_NAME]  
DATABAZE_NAME  

5) Запустить run.bat.