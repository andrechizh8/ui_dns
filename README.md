## :heavy_check_mark: В проекте реализованы следующие проверки:

:radio_button: Авторизация на сайте с помощью логин/пароль

:radio_button: Поиск товара

:radio_button: Добавление товара в избранное

:radio_button: Редактирование данных пользователя

:radio_button: Отправка отзыва о работе сайта

:radio_button: Изменение геолокации

---
Общая настройка для запуска тестов :

В командной строке прописать :
- pip install poetry

- poetry lock

- poetry install 

Для запуска тестов локально необходимо :

1. В файле .env определить логин и пароль для сайта www.dns-shop.ru
  
2. Удалить параметр autouse=true из фикстуры selenoid_config в файлe conftest.py

3. В командной строке прописать: pytest .

---

Для запуск тестов с помощью Selenoid необходимо:

1. В файле .env определить :
 
       1.1 Логин и пароль для сайта www.dns-shop.ru
  
       1.2 Логин и пароль для Selenoid
       
  
2. Прописать параметр autouse=true в фикстуру selenoid_config в файле conftest.py

3. В командной строке прописать: pytest .

---
 ### Запуск в Jenkins : [JOB](https://jenkins.autotests.cloud/job/DNS/)
 
 Нажать на кнопку Собрать сейчас
![Альтернативный текст](https://github.com/andrechizh8/ui_dns/blob/main/readme%20files/dns1.png)

После сборки есть возможность посмотреть отчет с различными приложениями: 

Скриншот:

![Альтернативный текст](https://github.com/andrechizh8/ui_dns/blob/main/readme%20files/dns2.png)

Cсылка на Allure report : [Report](https://jenkins.autotests.cloud/job/DNS/60/allure/)

Видео :

![Альтернативный текст](https://github.com/andrechizh8/ui_dns/blob/main/readme%20files/dns.gif)

Кроме того, в проекте реализована возможность просмотр отчета в  Allure TestOps : 

![Альтернативный текст](https://github.com/andrechizh8/ui_dns/blob/main/readme%20files/dns4.png)

И интеграция с Jira :

![Альтернативный текст](https://github.com/andrechizh8/ui_dns/blob/main/readme%20files/dns5.png)

После прохождения тестов с использованием Jenkins, в телеграмм приходит оповещение с результатами :

![Альтернативный текст](https://github.com/andrechizh8/ui_dns/blob/main/readme%20files/dns_telegram.png)
