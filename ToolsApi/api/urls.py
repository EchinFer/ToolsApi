from django.urls import path
from .views import OcrView

urlpatterns=[
    path('getTextFromImage', OcrView.as_view(), name="text_from_image")
]
