from django.contrib import admin
from .models import Cursos


# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    list_display = ('titulo_curso','descripcion','categoria', 'costo',)
    search_fields = ('titulo_curso','descripcion','categoria', 'costo')
    date_hierarchy = 'created'
    list_filter = ('titulo_curso', 'costo')

admin.site.register(Cursos, AdministrarModelo)


