
from django.shortcuts import render, HttpResponse

# Create your views here.

def principal(request):
    return render(request, "contenido/principal.html")

def cursos(request):
    return render(request,"contenido/cursos.html")

def contacto(request):
    return render(request, "contenido/contacto.html")

def ejemplo(request):
    contenido=""""""
    return render(request, "contenido/ejemplo.html")

def prueba(request):
    contenido=""""""
    return render(request, "contenido/prueba.html")