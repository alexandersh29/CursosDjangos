from contenido.views import cursos
from django.shortcuts import render
from .models import Cursos
from .forms import ConsultaCursoForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
# Create your views here.

def registros(request):
    cursos = Cursos.objects.all()
    return render(request, "registros/principal.html", {'cursos': cursos})

def consultarCursos(request):
    cursos = Cursos.objects.all()
    return render(request, "registros/consultaCursos.html", {'cursos': cursos})

def registrar(request):
    if request.method == 'POST':
        form = ConsultaCursoForm(request.POST, request.FILES)
        if form.is_valid():
            cursos = Cursos.objects.all()
            titulo_curso = request.POST['titulo_curso']
            descripcion = request.POST['descripcion']
            duracion = request.POST['duracion']
            categoria = request.POST['categoria']
            costo = request.POST['costo']
            estado = request.POST['estado']
            imagen = request.FILES['imagen']
            insert = Cursos(titulo_curso=titulo_curso, descripcion=descripcion, duracion=duracion,
                            categoria=categoria, costo=costo, estado=estado, imagen=imagen)
            insert.save()
            return render(request, "registros/consultaCursos.html", {'cursos': cursos})
        else:
            messages.error(request, "Error al procesar el formulario")
    form = ConsultaCursoForm()
    return render(request, 'registros/crearCurso.html', {'form': form})


def contacto(request):
    return render(request, "registros/crearCurso.html")


def contactoF(request):
    return render(request, "contenido/contacto.html")


def eliminarCurso(request, id, confirmacion='registros/confirmarEliminacion.html'):
    curso = get_object_or_404(Cursos, id=id)
    if request.method == 'POST':
        curso.delete()
        cursos = Cursos.objects.all()
        return render(request, "registros/consultaCursos.html", {'cursos': cursos})

    return render(request, confirmacion, {'object': curso})


def consultarCursoIndividual(request, id):
    curso = Cursos.objects.get(id=id)

    return render(request, "registros/formEditarCurso.html", {'curso': curso})


def editarCurso(request, id):
    curso = get_object_or_404(Cursos, id=id)
    form = ConsultaCursoForm(request.POST, request.FILES, instance=curso)

    if form.is_valid():
        form.save()  # si el registro ya existe, se modifica.
        cursos = Cursos.objects.all()
        return render(request, "registros/consultaCursos.html", {'cursos': cursos})

    return render(request, "registros/formEditarCurso.html", {'curso': curso})
