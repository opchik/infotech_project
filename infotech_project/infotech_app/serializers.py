from rest_framework import serializers

from .models import Data
from .validators import validate_file_type


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField(required=True, validators=[validate_file_type])





