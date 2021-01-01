from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from photos.models import Photo
from photos.serializers import PhotoSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def photo_list(request):
    if request.method == 'GET':
        photos = Photo.objects.all()
        
        uuid = request.query_params.get('uuid', None)
        if uuid is not None:
            photos = photos.filter(uuid__icontains=uuid)
        
        photo_serializer = PhotoSerializer(photos, many=True)
        return JsonResponse(photo_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        photo_data = JSONParser().parse(request)
        photo_serializer = PhotoSerializer(data=photo_data)
        if photo_serializer.is_valid():
            photo_serializer.save()
            return JsonResponse(photo_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(photo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Photo.objects.all().delete()
        return JsonResponse({'message': '{} Photos were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def photo_detail(request, pk):
    try: 
        photo = Photo.objects.get(pk=pk) 
    except Photo.DoesNotExist: 
        return JsonResponse({'message': 'The photo does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        photo_serializer = PhotoSerializer(photo) 
        return JsonResponse(photo_serializer.data) 
 
    elif request.method == 'PUT': 
        photo_data = JSONParser().parse(request) 
        photo_serializer = PhotoSerializer(photo, data=photo_data) 
        if photo_serializer.is_valid(): 
            photo_serializer.save() 
            return JsonResponse(photo_serializer.data) 
        return JsonResponse(photo_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        photo.delete() 
        return JsonResponse({'message': 'Photo was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def photo_list_published(request):
    photos = Photo.objects.filter(published=True)
        
    if request.method == 'GET': 
        photo_serializer = PhotoSerializer(photos, many=True)
        return JsonResponse(photo_serializer.data, safe=False)