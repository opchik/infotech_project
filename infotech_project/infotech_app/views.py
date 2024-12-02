from .models import Data
from .serializers import DataSerializer, FileUploadSerializer
from .validators import validate_data

from django.shortcuts import render
import pandas as pd
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    method='post',
    request_body=FileUploadSerializer,
    responses={200: 'File uploaded successfully'}
)
@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_file(request):
    serializer = FileUploadSerializer(data=request.data)
    if serializer.is_valid():
        file = serializer.validated_data['file']
        try:
            df = pd.read_excel(file)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        for _, row in df.iterrows():
            data = validate_data(row.to_dict())
            serializer = DataSerializer(data)
            Data.objects.create(**serializer.data)
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_data_json(request):
    data = Data.objects.all()
    serializer = DataSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_data_html(request):
    data = Data.objects.all()
    return render(request, 'infotech_app/index.html', {'data': data})

