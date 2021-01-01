from django.conf.urls import url 
from photos import views 
 
urlpatterns = [ 
    url(r'^api/photos$', views.photo_list),
    url(r'^api/photos/(?P<pk>[0-9]+)$', views.photo_detail),
    url(r'^api/photos/published$', views.photo_list_published)
]