# Generated by Django 3.2.4 on 2021-08-06 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0017_remove_consultacurso_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultacurso',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografía'),
        ),
    ]