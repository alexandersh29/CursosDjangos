# Generated by Django 3.2.4 on 2021-08-07 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0024_alter_cursos_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='categoria',
            field=models.CharField(max_length=50, verbose_name='Categoría del curso'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='duracion',
            field=models.CharField(max_length=100, verbose_name='Duración del curso'),
        ),
    ]
