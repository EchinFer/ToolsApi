from django.shortcuts import render
from django.views import View
import pytesseract 
from PIL import Image
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from textblob import TextBlob
import cv2
import numpy as np
from language_tool_python import LanguageTool

# Create your views here.

class OcrView(View):
    
    def post(self, request):
        text = ""
        text_correction = ""
        if request.method == 'POST' and request.FILES.get('image'):
            # Leer los datos binarios de la imagen
            image_data = request.FILES['image']

            # Convertir los datos binarios a una matriz NumPy
            image = cv2.imdecode(np.fromstring(image_data.read(), np.uint8), cv2.IMREAD_COLOR)

            # Convertir a escala de grises
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Aplicar umbralización
            _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            
            # Realiza OCR en la imagen usando Tesseract a través de pytesseract            
            text = pytesseract.image_to_string(thresholded, lang='spa')

            tool = LanguageTool('es')
            #correcciones = tool.check(text)
            text_correction = LanguageTool.correct(tool, text)
            #text_correction = TextBlob(text)
            #text_correction = str(text_correction.correct())
            
        
        return JsonResponse({'text': text_correction, 'originalText': text})

    def put(self, request):
        pass

    def delete(self, request):
        pass 