# Generated by Django 2.2 on 2019-10-01 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_auto_20190930_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maquinaria',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='maquinaria',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='maquinaria',
            name='tipo',
        ),
    ]
