from django import forms
from django.db import models
from django.forms.models import fields_for_model
from .models import Cursos
from django.forms import ModelForm, ClearableFileInput, widgets

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br> <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

class ConsultaCursoForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ['titulo_curso','descripcion','duracion','categoria','costo','estado','imagen']
        widgets = {
            'imagen': CustomClearableFileInput
        }