#!/bin/bash

python manage.py makemigrations photos 
python manage.py migrate photos 
