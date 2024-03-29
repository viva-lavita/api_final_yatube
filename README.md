# RESTful API Yatube
Yatube - социальная сеть для публикации записей и общения пользователей, этот репозиторий - api-функционал к этой соцсети.

С помощью api_yatube можно запрашивать данные о постах, группах, комментариях, а также создавать новые.

## Стек технологий

* [Python 3.9](https://www.python.org/)
* [Django 3.2](https://www.djangoproject.com/)
* [Django REST framework](www.django-rest-framework.org/)
* [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io)
* [Djoser](https://djoser.readthedocs.io)

## Документация 

Документация по проекту после запуска сервера доступна по адресу:
http://127.0.0.1:8000/redoc/

### Как запустить проект:

Ниже представлены команды, которые нужно запускать через консоль(командную строку).
(прим. Командная строка (иначе — терминал или консоль) — это программа, которая позволяет управлять компьютером посредством текстовых команд.)

Пожалуйста обратите внимание, команды представлены для версии терминала Git Bash, в операционных системах Linux и MacOS она установлена по умолчанию, в ОП Windows же ее нужно установить дополнительно [отсюда](https://gitforwindows.org/). 

Обратите внмиание, для старых версий Linux команды могут отличаться, в качестве проверки введите в терминал команду:

```bach
python --version
```

Если ответ будет формата Python 2.x.x, при запуске команд из документации вам нужно будет 'явно' обращаться к третьей версии python, это можно сделать добавляя к команде python цифру 3, пример:

```bash
python3 -m venv venv
```

## Запуск проекта в dev-режиме

- Клонируйте репозиторий и перейдите в него в командной строке.
- Установите и активируйте виртуальное окружение c учетом версии Python 3.9 (выбираем python не ниже 3.7):

```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

```bash
python -m pip install --upgrade pip
```

- Затем нужно установить все зависимости из файла requirements.txt

```bash
cd yatube_api
```

```bash
pip install -r requirements.txt
```

- Выполняем миграции:

```bash
python manage.py migrate
```

- Создаем суперпользователя:

```bash
python manage.py createsuperuser
```

- Запускаем проект:

```bash
python manage.py runserver
```

## Работа с API для всех пользователей

Для неавторизованных пользователей работа с API доступна в режиме чтения, что-либо изменить или создать не получится.

## Доступные эндпоинты и методы:

```r
GET, POST  api/v1/posts/ - получить список всех публикаций, создание новых публикаций
При указании параметров limit и offset выдача должна работать с пагинацией
GET, PUT, PATCH, DELETE  api/v1/posts/{id}/ - получение, обновление, удаление публикации по id
GET  api/v1/groups/ - получение списка сообществ
GET  api/v1/groups/{id}/ - получение информации о сообществе по id
GET, POST  api/v1/{post_id}/comments/ - получение всех комментариев к публикации
GET, PUT, PATCH, DELETE  api/v1/{post_id}/comments/{id}/ - получение, обновление, удаление комментария к публикации по id
GET, POST  api/v1/follow/ - получить список всех подписок автора запроса, создание новых подписок
POST  api/v1/jwt/create/ - создание JWT-токена
POST  api/v1/jwt/refresh/ - обновление JWT-токена
POST  api/v1/jwt/verify/ - проверить JWT-токен
```

## Примеры работы с API для авторизованных пользователей

- Для создания публикации используем:

```r
POST /api/v1/posts/
```

в body запроса

```json
{
    "text": "string",
    "image": "string",
    "group": 0
}
```
в body ответа

```json
[
    {
        "id": 0,
        "author": "string",
        "image": "string",
        "text": "string",
        "pub_date": "2019-08-24T14:15:22Z",
        "group": 0
    },
...
]
```

- Обновление публикации:

```r
PUT /api/v1/posts/{id}/
```

в body

```json
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

в body ответа

```json
{
    "id": 0,
    "author": "string",
    "image": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "group": 0
}
```

- Удаление публикации:

```r
DEL /api/v1/posts/{id}/
```

Получение доступа к эндпоинту /api/v1/follow/ (подписки) доступен только для авторизованных пользователей.

Подписка пользователя от имени которого сделан запрос, на пользователя переданного в теле запроса. Анонимные запросы запрещены.

```r
GET /api/v1/follow/
```

в body

```r
{
    "following": "string"
}
```

в body ответа

```r
{
    "id": 0,
    "user": "string",
    "following": "string"
}
```

- Добавление комментария:

```r
GET api/v1/posts/{post_id}/comments/
```

в body

```r
{
    "text": "string"
}
```

в body ответа

```r
{
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
}
```
## Добавить группу в проект нужно через админ панель Django:

после авторизации, переходим в раздел Groups и создаем группы.

```r
admin/
```

- Доступ авторизованным пользователем доступен по JWT-токену (Joser), который можно получить выполнив POST запрос по адресу:

```r
POST /api/v1/jwt/create/
```

- Передав в body данные пользователя (например в postman):

```json
{
    "username": "string",
    "password": "string"
}
```

в body ответа два ключа: 

```json
{
    "refresh": "string",
    "access": "string"
}
```

Токен вернётся в поле access, а данные из поля refresh пригодятся для обновления токена. 

- Полученный токен (значение по ключу "access") добавляем в Headers (postman), после чего буду доступны все функции проекта:

```r
Authorization: Bearer {your_token}
```

Если ваш токен утрачен, украден или каким-то иным образом скомпрометирован, вам понадобится отключить его и получить новый. Для этого отправьте POST-запрос на тот же адрес /auth/jwt/create/, а в теле запроса в поле refresh передайте refresh-токен. 

- Обновить JWT-токен:

```r
POST /api/v1/jwt/refresh/
```

- Проверить JWT-токен:

```r
POST /api/v1/jwt/verify/
```

- Так же в проекте API реализована пагинация (LimitOffsetPagination):

```r
GET /api/v1/posts/?limit=5&offset=0
```
