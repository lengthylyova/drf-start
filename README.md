# ![drf-start - Application template](https://img.shields.io/static/v1?label=drf-start&message=Application+template&color=%23478CBF&style=for-the-badge&logo=django&logoColor=%23fff) 📦️
[![Tests](https://github.com/lengthylyova/drf-template/actions/workflows/tests.yml/badge.svg)](https://github.com/lengthylyova/drf-template/actions/workflows/tests.yml)
[![Build - Docker](https://img.shields.io/badge/Build-Docker-3496ed?logo=docker&logoColor=fff)](https://swagger.io/docs/specification/about/)
[![GitHub - Actions](https://img.shields.io/badge/GitHub-Actions-181717?logo=github&logoColor=fff)](https://github.com/features/actions)

[![Reverse proxy - nginx](https://img.shields.io/static/v1?label=Reverse+proxy&message=NGINX&color=%23009639&logo=nginx&logoColor=%23fff)](https://www.nginx.com/)
[![Django - REST Framework](https://img.shields.io/badge/Django-REST_Framework-A30000?logo=django&logoColor=fff)](https://www.django-rest-framework.org/)
[![Database - PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-4169e1?logo=postgresql&logoColor=fff)](https://www.postgresql.org/)

[![OpenAPI - Swagger](https://img.shields.io/badge/OpenAPI-Swagger-85EA2D?logo=swagger&logoColor=fff)](https://swagger.io/docs/specification/about/)

## Description 🔍️
**`drf-start`** - template designed for accelerated initial setup of your drf service. The template is fully dockerized with a swagger connected, nginx as a reverse-proxy and automated testing using GitHub Actions. ***What else do you need for an easy start?***

The template already contains a `users` app, with prewritten tests. You can leave it and modify it as you need or simply delete it.

I will be glad if you offer your own solutions to improve this template. ***Feedback is very important.***

## Usage 🚀

#### **Clone** repository:
```shell
git clone https://github.com/lengthylyova/drf-template.git
```

#### **Build** images **and Up** containers:
```shell
docker compose up --build
```

#### **Run** `manage.py` **commands**:
```shell
# For example createsuperuser
docker compose run --rm drfs-django python manage.py createsuperuser
```