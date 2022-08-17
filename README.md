# BloodFuse Backend Project

Reprehenderit mollit sint pariatur incididunt esse ea aliqua eiusmod. Do officia reprehenderit id exercitation ad. Eu occaecat ex labore Lorem qui id esse elit cillum. Mollit tempor sint est esse deserunt commodo laboris laboris quis.

# Technologies Used

- Programming Language: [**Python**](https://www.python.org)
- Framework: [**Django RestFramework (DRF)**](https://www.https://www.django-rest-framework.org/)
- Database: **Sqlite3**
- Development Hosting: [**PythonAnywhere**](https://www.pythonanywhere.com)

# Project Setup

Clone project

```console
git clone https://github.com/bloodfuse/backend/
```

Setup dev environment

```console
cd ./backend
pipenv install
pipenv shell
```

Start django server **(Linux/Mac)**

```console
python3 manage.py runserver
```

Start django server **(Windows)**

```console
python manage.py runserver
```

# API Endpoints URLs


- ## [Endpoints](https://bloodfuse.pythonanywhere.com/swagger/)
- ## [Docs](https://bloodfuse.pythonanywhere.com/redoc/)
- ## [Json](https://bloodfuse.pythonanywhere.com/swagger.json)
- ## [Yaml](https://bloodfuse.pythonanywhere.com/swagger.yaml)
-

# API Endpoints Docs

## Base Url

```console
https://bloodfuse.pythonanywhere.com/api/
```

## Authentication Endpoinsts
<!--
    [REGISTRATION]  ---------------------------------
 -->

- ### [/registration](#post-registration)
- ### [/token](#post-token)
- ### [/auth/login](#post-authlogin)
- ### [/auth/password/reset/]()

----------

### POST [/registration/](https://bloodfuse.pythonanywhere.com/api/registration/)
#### Request

```markdown
#DESCRIPTION
Bloodfuse registration API requires some parameters to be passed as a post request.

#REQUIRED FIELDS
email, user_name, account_type, fullname, blood_group, password_1, password_2.

The account_type is of two options "donor" or "recipient", likwise the blood_group parameter also have some options to choose from, "O+", "O-", "A-", "A+", "B-", "B+", "AB-", "AB+".
When passing password_1 and password_2 both parameters must be the same else a 404 error is thrown.
```

```json
parameters: {
    "email":  "example@email.com",
    "username": "user1",
    "account_type": "donor",
    "fullname":  "Thomas Edison",
    "blood_group": "O+",
    "password1": "1234567",
    "password2": "1234567"
}
```

#### Response

```json
method: GET,
response: {
    "email":  "example@email.com",
    "username": "user1",
    "account_type": "donor",
    "fullname":  "Thomas Edison",
    "blood_group": "O+",
}
```
=======
- ### [Endpoints](https://bloodfuse.pythonanywhere.com/swagger/)
- ### [Docs](https://bloodfuse.pythonanywhere.com/redoc/)
- ### [Json](https://bloodfuse.pythonanywhere.com/swagger.json)
- ### [Yaml](https://bloodfuse.pythonanywhere.com/swagger.yaml)


<!--
    [GET TOKENS]  ---------------------------------
 -->

## POST [token/](https://bloodfuse.pythonanywhere.com/api/token)

```json
description:
```

### Request

```json
parameters: {
    "email":  "example@exmaple.com",
    "password": "1234567890"
}
```

### Response

```json
method: GET
status: 200
response: {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MDg0ODQxNCwiaWF0IjoxNjYwNzYyMDE0LCJqdGkiOiI0MDMzNmVjYWNiMDk0YzBlYmU1OWJjZWY3MmM2OTdjZSIsInVzZXJfaWQiOiJkNDZiMTRmYy02MjAyLTRmMzktODNhNi00OWRjMWYxMDY3NmIifQ.TtCTWmtiRYsNiNmsrKeoDssIhCRE5eAToKuW9ZP-Mgs",

    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwNzYyMzE0LCJpYXQiOjE2NjA3NjIwMTQsImp0aSI6ImUzMzRiYTFhODEzZTQxNzg5OTYyMjAzZjA5MzQ4OWYxIiwidXNlcl9pZCI6ImQ0NmIxNGZjLTYyMDItNGYzOS04M2E2LTQ5ZGMxZjEwNjc2YiJ9.4bdAPjRWKaJS6gb_le8A08Q_ri_tBM5ItRAuPtCOTJI"
}
```

<!--
    [LOGIN] ---------------------------------
 -->

## POST [auth/login/](https://bloodfuse.pythonanywhere.com/api/auth/login/)

```json
description:
```

### Request

```json
request: {
    "email":  "example@email.com",
    "password": "1234345"
}
```

### Response

```json
method: GET
status: 200
response: {
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwNzY0NjM4LCJpYXQiOjE2NjA3NjQzMzgsImp0aSI6IjEwNDRiZTk0MmY4ODQwYjliMzFiNzMzYzZiOTZjZDA1IiwidXNlcl9pZCI6ImQ0NmIxNGZjLTYyMDItNGYzOS04M2E2LTQ5ZGMxZjEwNjc2YiJ9.KJsAKSK5StY72avNNWbhPZcsvBnUCXci4c3OBbj9wDs",

  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MDg1MDczOCwiaWF0IjoxNjYwNzY0MzM4LCJqdGkiOiI5NGEyMDViNTQzMzQ0ZTI4Yjk0YTY4MjFlZmRkMTkzZSIsInVzZXJfaWQiOiJkNDZiMTRmYy02MjAyLTRmMzktODNhNi00OWRjMWYxMDY3NmIifQ.0FTLJwSJZvt02X0zwdnEM6gluLSHE3SL_BJAnBA-Hzc",

  "user": {
    "pk": "d46b14fc-6202-4f39-83a6-49dc1f10676b",
    "email": "gaddiel@gmail.com",
    "first_name": "",
    "last_name": ""
  }
}
```
