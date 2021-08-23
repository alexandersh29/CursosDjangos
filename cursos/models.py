from django.db import models

# Create your models here.
class Cursos(models.Model): #Define la estructura de nuestra tabla
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    titulo_curso = models.TextField(verbose_name="Titulo del Curso")
    descripcion = models.TextField(verbose_name="Descripción del curso")
    duracion = models.CharField(max_length=100, verbose_name="Duración del curso")
    categoria = models.CharField(max_length=50, verbose_name="Categoría del curso")
    costo = models.FloatField(verbose_name="Costo del curso")
    estado = models.BooleanField(verbose_name="Curso activo")
    imagen = models.FileField(null=True, upload_to="fotos", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]
    
    def __str__(self):
        return self.titulo_curso



