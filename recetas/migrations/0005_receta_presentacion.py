# Generated by Django 5.2.3 on 2025-06-28 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0004_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='presentacion',
            field=models.TextField(blank=True, null=True, verbose_name='Presentación o notas adicionales'),
        ),
    ]
