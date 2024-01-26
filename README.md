# Django

## Version
```shell
Python 3.9.18
```
## Create venv
```shell
python -m venv venv
```

## Active venv
```shell
source ./venv/bin/activate
```

## Start django project
```shell
django-admin startproject djangoCeleryDemo
```

## Create new app
```shell
python manage.py startapp worker
```

## Install dependency
```shell
pip install celery
```

## Update requirements.txt
```shell
pip freeze > requirements.txt
```

## Install from requirements.txt
```shell
pip install -r requirements.txt
```

## Run server
```shell
python manage.py runserver 0.0.0.0:8000
```

## Run shell
```shell
python manage.py shell
```

## Trigger task from shell
```shell
from worker.tasks import execute_sync
execute_sync()
```

## Run celery
```shell
celery -A djangoCeleryDemo worker --hostname=worker1 -l INFO
```

## Run flower
```shell
celery -A djangoCeleryDemo flower -l INFO
```

## View flower
```shell
http://localhost:5555/
```

## Run postgres and redis
```shell
docker-compose up -d --build 
```

## Apply migrate
```shell
python manage.py migrate
```