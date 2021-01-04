from photos.models import Photo
from rest_framework.serializers import Serializer, ModelSerializer, FileField
 
 
class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id',
                'uuid',
                'content',
                'upload_time')

# Serializers define the API representation.
class UploadSerializer(Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']