# Create Project
```
python --version
```

## Сeate venv - віртуальне середоще для вашого проекту і пакетів
```
py -m venv .venv
python -m venv .venv
python3 -m venv .venv
```

## Activate venv
```
.venv\Scripts\activate.bat
source ./.venv/bin/activate

python.exe -m pip install --upgrade pip
python3 -m pip install --upgrade pip

py -m pip install Django
python -m pip install Django

py

>>>import django
>>>print(django.get_version())
>>>quit()

python -m django --version
mkdir atbmvt
django-admin startproject mysite atbmvt
cd atbmvt
py manage.py runserver 9581
```

## Install Postgres
```
pip install psycopg2-binary
py manage.py migrate
python3 manage.py migrate
```

## Додаю superuser
```
python manage.py createsuperuser
py manage.py createsuperuser
admin
123456
py manage.py runserver 9581
```