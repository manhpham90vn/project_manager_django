# Django

## Version
```shell
Python 3.9.18
```

## ENV
### Create venv
```shell
python -m venv venv
```

### Active venv
```shell
source ./venv/bin/activate
```

### Install dependency
```shell
pip install celery
```

### Update requirements.txt
```shell
pip freeze > requirements.txt
```

### Install from requirements.txt
```shell
pip install -r requirements.txt
```

### Run celery worker 1
```shell
celery -A projectmanager worker --hostname=worker1 -l INFO
```

### Run celery worker 2
```shell
celery -A projectmanager worker --hostname=worker2 -l INFO
```

### Run flower
```shell
celery -A projectmanager flower -l INFO
```

### View flower
```shell
http://localhost:5555/
```

### Run postgres and redis
```shell
docker-compose up -d --build 
```

### Run server
```shell
python manage.py runserver 0.0.0.0:8000
```

## DJANGO
### Start django project
```shell
django-admin startproject djangoCeleryDemo
```

### Create new app
```shell
python manage.py startapp worker
```

### Run shell
```shell
python manage.py shell
```

### Trigger task from shell
```shell
from worker.tasks import invoke_lambda
invoke_lambda.delay()
```

### Apply migrate
```shell
python manage.py migrate
```

### Create super user
```shell
python manage.py createsuperuser
```