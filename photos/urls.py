from django.conf.urls import url 
from rest_framework.authtoken.views import obtain_auth_token
from photos import views 
from django.urls import path

urlpatterns = [ 
    url(r'^api/photos$', views.photo),
    # url(r'^api/photos$', views.photo_upload),
    # url(r'^api/photos/(?P<filename>[^/]+)$', PhotosView.as_view()),
    # url(r'^api/photos$', PhotosView.as_view()),
    # url(r'^api/photos/(?P<pk>[0-9]+)$', views.photo_detail)
    path('token', obtain_auth_token, name='token'),
]