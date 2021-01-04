#!/bin/bash

# https://www.django-rest-framework.org/api-guide/authentication/#json-web-token-authentication
python manage.py migrate 
python manage.py makemigrations photos 
python manage.py migrate photos 
python manage.py createsuperuser
