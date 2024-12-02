from django.urls import path
from .views import get_data_json, get_data_html, upload_file

urlpatterns = [
    path('upload/', upload_file, name='upload-xls'),
    path('data/json/', get_data_json, name='get_data_json'),
    path('data/html/', get_data_html, name='get_data_html'),
]
