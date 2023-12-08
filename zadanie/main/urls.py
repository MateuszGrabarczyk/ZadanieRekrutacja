from django.urls import path
from .views import file_upload

urlpatterns = [
    path('', file_upload, name='file_upload'),
]