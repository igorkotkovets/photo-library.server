Tutorial page:
https://bezkoder.com/django-rest-api/#Django_Rest_Api_application_Overview

Upload file:
https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
https://www.django-rest-framework.org/api-guide/parsers/#fileuploadparser
https://www.goodcode.io/articles/django-rest-framework-file-upload/




INSTALLATION:
$ python manage.py makemigrations photos
$ python manage.py migrate photos
$ python manage.py runserver 8080


API:
$ curl -X GET http://127.0.0.1:8080/api/photos
* Upload image
$ curl -d "@2.txt" -X POST -H 'Content-Disposition: attachment; filename=upload.jpg' http://127.0.0.1:8080/api/photos

