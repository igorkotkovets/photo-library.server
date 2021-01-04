from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.parsers import FileUploadParser
from rest_framework import status
 
from photos.models import Photo
from photos.serializers import PhotoSerializer

import os
from django.http import StreamingHttpResponse
import logging
from rest_framework.exceptions import ParseError

from rest_framework.response import Response


from django.http import HttpResponse
from django.views import View

class PhotosView(View):
    parser_class = (FileUploadParser,)
    def get(self, request, format=None):
        logger = logging.getLogger('/api/photos')
        photos = Photo.objects.all()   
        uuid = request.GET.get('uuid', None)
        if uuid is not None:
            photos = photos.filter(uuid__icontains=uuid)
        
        photo_serializer = PhotoSerializer(photos, many=True)
        return JsonResponse(photo_serializer.data, safe=False)


    def post(self, request, format=None):
        logger = logging.getLogger('/api/photos')
        if 'file' not in request.data:
            return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

        f = request.data['file']
        filename = f.name
        photo = Photo.objects.create(name=filename)
        photo.content.save(filename, f, save=True)
        photo_serializer = PhotoSerializer(photo)

        return JsonResponse(photo_serializer.data, status=status.HTTP_201_CREATED)


    def delete(self, request, format=None):
        logger = logging.getLogger('/api/photos')
        count = Photo.objects.all().delete()    
        return JsonResponse({'message': '{} Photos were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)