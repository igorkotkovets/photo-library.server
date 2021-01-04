from django.conf.urls import url 
from photos import views 

urlpatterns = [ 
    url(r'^api/photos$', views.photo),
    # url(r'^api/photos$', views.photo_upload),
    # url(r'^api/photos/(?P<filename>[^/]+)$', PhotosView.as_view()),
    # url(r'^api/photos$', PhotosView.as_view()),
    # url(r'^api/photos/(?P<pk>[0-9]+)$', views.photo_detail)
]