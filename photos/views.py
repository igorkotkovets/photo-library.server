from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.parsers import FileUploadParser
from rest_framework import status
 
from photos.models import Photo
from photos.serializers import PhotoSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import parser_classes

import os
from django.http import StreamingHttpResponse
import logging
from rest_framework.exceptions import ParseError

from rest_framework.response import Response

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
@parser_classes([FileUploadParser])
def photo(request):
    logger = logging.getLogger('/api/photos')

    if request.method == 'GET':
        photos = Photo.objects.all()
        
        uuid = request.query_params.get('uuid', None)
        if uuid is not None:
            photos = photos.filter(uuid__icontains=uuid)
        
        photo_serializer = PhotoSerializer(photos, many=True)
        return JsonResponse(photo_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        logger = logging.getLogger('/api/photos')
        if 'file' not in request.data:
            return JsonResponse(photo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        f = request.data['file']
        filename = f.name
        photo = Photo.objects.create(name=filename)
        photo.content.save(filename, f, save=True)
        photo_serializer = PhotoSerializer(photo)

        return JsonResponse(photo_serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'DELETE':
        count = Photo.objects.all().delete()
        return JsonResponse({'message': '{} Photos were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)