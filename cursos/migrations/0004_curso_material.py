# Generated by Django 3.2.15 on 2022-08-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_curso_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='material',
            field=models.URLField(default='URL do material'),
        ),
    ]
