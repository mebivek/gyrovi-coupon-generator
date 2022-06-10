# Gyrovi Test Coupon 

Gyrovi interview test- a coupon generator


## Pre Requisites
- python >= 3.8
- virtualenv (a python package)
- docker (for swagger documentation)

## Host Swagger doc

First enter following command
```
docker run -p 5500:8080 -e SWAGGER_JSON=/api.yaml -v /<Path-to-the-project>/swagger.yml:/api.yaml swaggerapi/swagger-ui
```

If permission denied error arise, please try using sudo.

After docker spins up the image, go to the browser and enter http://localhost:5500/

## Getting started

To get started, please run following commands

- cd to_project_path
- virtualenv venv
- source venv/bin/activate
- cd coupon_generator
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py create_demo_coupons
- python manage.py runserver 0.0.0.0:8000

Now go to the browser and open http://localhost:8000

