#!/bin/bash

python manage.py createsuperuser --username $1 --email $1@example.com
python manage.py drf_create_token $1 
