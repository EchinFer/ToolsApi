from django.shortcuts import render
from django.views import View
import pytesseract 
from PIL import Image
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class OcrView(View):
    
    def post(self, request):
        text = ''
        if request.method == 'POST' and request.FILES.get('image'):
            image = request.FILES['image']
        
            # Abre la imagen usando PIL (Python Imaging Library)
            img = Image.open(image)
            
            # Realiza OCR en la imagen usando Tesseract a través de pytesseract
            text = pytesseract.image_to_string(img)
        
        return JsonResponse({'text': text})

    def put(self, request):
        pass

    def delete(self, request):
        pass