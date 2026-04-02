@echo off

REM ==== API ====
cd djangoapi\postapi
docker build -t django-api-p32 .
docker tag django-api-p32:latest novakvova/django-api-p32:latest
docker push novakvova/django-api-p32:latest

REM ==== WEB ====
cd ..\..\my-post
docker build -t my-post --build-arg VITE_API_BASE_URL=http://3.126.91.162:4512 .
docker tag my-post:latest novakvova/my-post:latest
docker push novakvova/my-post:latest

echo DONE
pause
