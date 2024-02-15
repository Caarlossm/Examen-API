from django.shortcuts import render

# Create your views here.

# socios/views.py

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Socio
import json

@csrf_exempt
def introducir_socio(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nuevo_socio = Socio.objects.create(
            dni=data['dni'],
            numero_socio=data['numero_socio'],
            contraseña=data['contraseña']
        )
        return JsonResponse({'message': 'Socio creado correctamente'}, status=201)
    else:
        return JsonResponse({'message': 'Método no permitido'}, status=405)

@csrf_exempt
def modificar_socio(request, numero_socio):
    socio = get_object_or_404(Socio, numero_socio=numero_socio)
    if request.method == 'POST':
        data = json.loads(request.body)
        socio.contraseña = data['contraseña']
        socio.save()
        return JsonResponse({'message': 'Contraseña de socio modificada correctamente'}, status=200)
    else:
        return JsonResponse({'message': 'Método no permitido'}, status=405)

def obtener_todos_los_socios(request):
    socios = Socio.objects.all()
    data = [{'dni': socio.dni, 'numero_socio': socio.numero_socio, 'contraseña': socio.contraseña} for socio in socios]
    return JsonResponse(data, safe=False)
