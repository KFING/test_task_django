Задание:
1. Файл test.py в архиве. Запустить файл без ошибок(если выйдет). Подробные инструкции по выполнению внутри файла в каждом задании.
2. Создать в своём репазитории публичный Django проект. Реализовать авторизацию. В системе со старта должен быть пользователь:
    login: "4elovekconstanta@vought.com"
    password: "5uperP@sw00rd"

    На главной странице должна отображаться информация:
    1) Колличестве успешных авторизаций пользователя
    2) Колличество неуспешных 
    3) Процентное соотношение успешных и нет. Так же выделить стиль страницы в зависимости от большего значения

Так же в репазитории создать папку "task_1" куда положить исправленый файл из первого задания Предоставить ссылку на репазиторий. 
Конечно можно исполнение файла "test.py" с выводом результата и через страницу в проекте сделать... Но это уже по сугубо личному стремлению к прекрасному.
 
1. test.py запускается отдельно
2. Django проект после скачивания перед его запуском нужно сделать миграции и скачать все библиотеки из файла requirements.txt и после запустить контейнер с бд (docker compose up --build)
3. После можно запустить сам проект (python manage.py runserver)
