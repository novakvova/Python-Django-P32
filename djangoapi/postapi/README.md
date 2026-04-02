# Docker build project
```
pip freeze > requirements.txt

docker build -t django-api-p32 .

docker run --name django-container --restart=always -p 3456:8000 -d django-api-p32:latest
```


## Add Bat file project
```
@echo off

REM ==== API ====
cd djangoapi\postapi
docker build -t django-api-p32 .
docker tag django-api-p32:latest novakvova/django-api-p32:latest
docker push novakvova/django-api-p32:latest

echo DONE
pause
```

## Run projects server
```
docker compose up -d

docker compose pull

docker compose up -d
```