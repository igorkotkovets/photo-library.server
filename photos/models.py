from django.core.files.base import ContentFile
from django.db import models
from django.conf import settings

class Photo(models.Model):
    # uuid = models.CharField(max_length=255, blank=False)
    name = models.CharField(max_length=255, blank=False)
    content = models.FileField(upload_to='media', blank=False)
    upload_time = models.DateTimeField(auto_now_add=True)