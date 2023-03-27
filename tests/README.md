## :heavy_check_mark: В проекте реализованы следующие проверки:

:radio_button: Авторизация на сайте с помощью логин/пароль

:radio_button: Поиск товара

:radio_button: Добавление товара в избранное

:radio_button: Редактирование данных пользователя

:radio_button: Отправка отзыва о работе сайта

:radio_button: Изменение геолокации

---

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
