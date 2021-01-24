# PHOTO STORAGE APPLICATION

### Description 
Server application is developed to replace Google Photos cloud storage. Allows to backup photo library from iOS device to locally hosted file storage: it can be Raspberry Pi or another computer

Tutorial page:
https://bezkoder.com/django-rest-api/#Django_Rest_Api_application_Overview
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models


Upload file:
https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
https://www.django-rest-framework.org/api-guide/parsers/#fileuploadparser
https://www.goodcode.io/articles/django-rest-framework-file-upload/

Authorization:
https://www.django-rest-framework.org/api-guide/authentication/#setting-the-authentication-scheme
https://www.django-rest-framework.org/api-guide/permissions/



ADMIN WEBSITE:
http://127.0.0.1:8080/admin

#INSTALL ENVIRONMENT
$ python -m pip install Django
$ pip install djangorestframework
$ pip install django-cors-headers

INSTALLATION:
$ python manage.py makemigrations photos
$ python manage.py migrate photos
$ python manage.py runserver 8080

#CREATE USER
$ python manage.py createsuperuser --username vitor --email vitor@example.com


API:
$ curl -X GET http://127.0.0.1:8080/api/photos
* Upload image
$ curl -d "@2.txt" -X POST -H 'Content-Disposition: attachment; filename=upload.jpg' http://127.0.0.1:8080/api/photos



