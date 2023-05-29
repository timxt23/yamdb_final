# Проект API YaMDb

API YaMDb собирает отзывы пользователей на различные произведения такие как
фильмы, книги и музыка. 

## Описание проекта:
API YaMDb позволяет работать со следующими сущностями:
* JWT-токен (Auth): отправить confirmation_code на переданный email, получить
  JWT-токен
  в обмен на email и confirmation_code;
* Пользователи (Users): получить список всех пользователей, создать
  пользователя,
  получить пользователя по username, изменить данные пользователя по username,
  удалить
  пользователя по username, получить данные своей учётной записи, изменить
  данные своей учётной записи;
* Категории (Categories) произведений: получить список всех категорий, создать
  категорию, удалить категорию;
* Жанры (Genres): получить список всех жанров, создать жанр, удалить жанр;
* Произведения (Titles), к которым пишут отзывы: получить список всех объектов,
  создать
  произведение для отзывов, информация об объекте, обновить информацию об
  объекте, удалить произведение.
  пользователя по username, получить данные своей учётной записи, изменить
  данные своей учётной записи;
* Отзывы (Review): получить список всех отзывов, создать новый отзыв, получить
  отзыв по id,
  частично обновить отзыв по id, удалить отзыв по id;
* Комментарии (Comments) к отзывам: получить список всех комментариев к отзыву
  по id, создать новый комментарий для отзыва, получить комментарий для отзыва по id, частично
  обновить комментарий к отзыву по id, удалить комментарий к отзыву по id.

## Участники проекта:
[timxt23](https://github.com/timxt23) - управление пользователями (Auth и
Users): система регистрации и аутентификации, права доступа, работа с токеном,
система подтверждения e-mail, поля;

[chetvertakov](https://github.com/chetvertakov) - категории (Categories), жанры (Genres)
и произведения (Titles): модели, view и эндпойнты для них;

[nikliza](https://github.com/nikliza)  - отзывы (Review) и комментарии (Comments):
модели и view, эндпойнты, права доступа для запросов. Рейтинги произведений.

## Используемые технологии:
* Python3
* SQLite
* Django
* Django Rest Framework
* JSON Web Token

## Запуск проекта

Адрес: http://84.201.157.246

![example workflow](https://github.com/timxt23/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)


Клонирование репозитория
```
git@github.com:timxt23/infra_sp2.git
cd infra_sp2
```
Переходим в папку с файлом docker-compose.yaml:
```
cd infra
```
Поднимаем контейнеры (infra_db-1, infra_web-1, infra_nginx-1):
```
docker-compose up -d --build
```
Выполняем миграции:
```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```
Создаем суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```
Собираем статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```
Создаем дамп базы данных (нет в текущем репозитории):
```
docker-compose exec web python manage.py dumpdata > dumpPostrgeSQL.json
```
Останавливаем контейнеры:
```
docker-compose down -v
```

## Документация для YaMDb доступна по адресу:
```
http:/<ip_address>/redoc/
```

## Пример запроса к api:
Запрос:
```
http://<ip_address>:8000/api/v1/users/
```
Ответ:
```
{
    "count": 7,
    "next": null,
    "previous": null,
    "results": [
        {
            "username": "bingobongo",
            "email": "bingobongo@yamdb.fake",
            "first_name": "",
            "last_name": "",
            "bio": "",
            "role": "user"
        },
        {
            "username": "capt_obvious",
            "email": "capt_obvious@yamdb.fake",
            "first_name": "",
            "last_name": "",
            "bio": "",
            "role": "admin"
        },
        {
            "username": "faust",
            "email": "faust@yamdb.fake",
            "first_name": "",
            "last_name": "",
            "bio": "",
            "role": "user"
        },
        {
            "username": "reviewer",
            "email": "reviewer@yamdb.fake",
            "first_name": "",
            "last_name": "",
            "bio": "",
            "role": "user"
        },
        {
            "username": "angry",
            "email": "angry@yamdb.fake",
            "first_name": "",
            "last_name": "",
            "bio": "",
            "role": "moderator"
        }
    ]
}
```
