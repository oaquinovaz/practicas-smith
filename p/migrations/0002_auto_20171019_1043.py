# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejercitodelasmurallas',
            name='ejercito',
            field=models.CharField(choices=[('Policia Militar', 'Policia Militar'), ('Legion de Reconocimiento', 'Legion de Reconocimiento'), ('Tropas Estacionarias', 'Tropas Estacionarias')], max_length=24),
        ),
        migrations.AlterField(
            model_name='ejercitodelasmurallas',
            name='muralla',
            field=models.CharField(choices=[('Muralla Sina', 'Muralla Sina'), ('Muralla Maria', 'Muralla Maria'), ('Muralla Rose', 'Muralla Rose')], max_length=13),
        ),
        migrations.AlterField(
            model_name='guerrerosz',
            name='universo',
            field=models.CharField(choices=[('7', '7'), ('6', '6'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('2', '2'), ('1', '1'), ('8', '8'), ('3', '3'), ('5', '5'), ('4', '4')], max_length=2),
        ),
        migrations.AlterField(
            model_name='ninjas',
            name='nivelMilitar',
            field=models.CharField(choices=[('Anbu', 'Anbu'), ('Jonin', 'Jonin'), ('Chunin', 'Chunin'), ('Genin', 'Genin'), ('Kage', 'Kage'), ('Sannin', 'Sannin')], max_length=6),
        ),
    ]