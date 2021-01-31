# Куда пойти в Москве

Сайт содержит информацию о самых интересных местах Москвы.  

[Демо-версия сайта](http://pzhuchkov.pythonanywhere.com/)

## Запуск сайта

Для запуска сайта Python (версия >= 3.8) должен быть установлен.

1. Скачайте код с GitHub.  
   
2. Установите зависимости:
```console
pip install -r requirements.txt
```

3. Создайте базу данных SQLite:
```console
python manage.py migrate
```

4. Определите [переменные окружения](#переменные-окружения).
   
5. Создайте суперпользователя для доступа в административный интерфейс:
```console
python manage.py createsuperuser
```  
6. Для загрузки [тестовых данных](https://github.com/devmanorg/where-to-go-places/tree/master/places) можно использовать
   пользовательскую management-команду `load_place`:
```console
python manage.py load_place "{url-адрес JSON-файла из тестовых данных}"
```    
*Пример:*
```console
python manage.py load_place "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/Антикафе Bizone.json"
```   
7. Запустите разработческий сервер:
```console
python manage.py runserver
```  


## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 4 переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки
- `SECRET_KEY` — секретный ключ проекта
- `DATABASE_FILEPATH` — полный путь к файлу базы данных SQLite, например: `/home/user/schoolbase.sqlite3`
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)



## Цели проекта

Код написан в учебных целях — для курса по Python и веб-разработке на сайте [Devman](https://dvmn.org).  
Тестовые данные взяты с сайта [KudaGo](https://kudago.com/).
