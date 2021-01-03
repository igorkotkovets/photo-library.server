from django.conf.urls import url 
from photos import views 
 
urlpatterns = [ 
    # url(r'^api/photos$', views.photo_list),
    url(r'^api/photos$', views.photo_upload),
    url(r'^api/photos/(?P<filename>[^/]+)$', views.photo_upload)
    # url(r'^api/photos/(?P<pk>[0-9]+)$', views.photo_detail)
]