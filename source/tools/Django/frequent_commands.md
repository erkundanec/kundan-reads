---
title: Frequent Commands
description: Frequent Commands
sidebar_position: 1
---

```bash
.\django_env\Scripts\activate

python manage.py makemigrations 

python manage.py migrate

python manage.py runserver

python manage.py createsuperuser

pip freeze > requirement.txt

pip freeze > requirement.txt

gunicorn apipy.wsgi:application

waitress-serve --host=127.0.0.1 --port=8000 apipy.wsgi:application

python manage.py seed_data

python manage.py collectstatic
```
