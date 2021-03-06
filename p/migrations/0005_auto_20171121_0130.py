# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p', '0004_auto_20171114_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animes',
            name='genero',
            field=models.CharField(choices=[('Comedia', 'Comedia'), ('Misterio', 'Misterio'), ('Ciencia Ficción', 'Ciencia Ficción'), ('Militar', 'Militar'), ('Música', 'Música'), ('Policía', 'Policía'), ('Psicológico', 'Psicológico'), ('Recuentros de la vida', 'Recuentros de la vida'), ('Demonios', 'Demonios'), ('Espacial', 'Espacial'), ('Shounen', 'Shounen'), ('Yaoi', 'Yaoi'), ('Carreras', 'Carreras'), ('Demencia', 'Demencia'), ('Ecolares', 'Ecolares'), ('Parodia', 'Parodia'), ('Historico', 'Historico'), ('Infantil', 'Infantil'), ('Samurai', 'Samurai'), ('Terror', 'Terror'), ('Mecha', 'Mecha'), ('Fantasía', 'Fantasía'), ('Ecchi', 'Ecchi'), ('Superpoeders', 'Superpoeders'), ('Yuri', 'Yuri'), ('Sobrenatural', 'Sobrenatural'), ('Romance', 'Romance'), ('Seinen', 'Seinen'), ('Acción', 'Acción'), ('Suspenso', 'Suspenso'), ('Aventuras', 'Aventuras'), ('Jegos', 'Jegos'), ('Artes Marciales', 'Artes Marciales'), ('Shoujo', 'Shoujo'), ('Josei', 'Josei'), ('Harem', 'Harem'), ('Magia', 'Magia'), ('Vampiros', 'Vampiros'), ('Deportes', 'Deportes'), ('Drama', 'Drama')], max_length=21),
        ),
        migrations.AlterField(
            model_name='ejercitodelasmurallas',
            name='muralla',
            field=models.CharField(choices=[('Muralla Maria', 'Muralla Maria'), ('Muralla Sina', 'Muralla Sina'), ('Muralla Rose', 'Muralla Rose')], max_length=13),
        ),
        migrations.AlterField(
            model_name='guerrerosz',
            name='universo',
            field=models.CharField(choices=[('2', '2'), ('3', '3'), ('7', '7'), ('4', '4'), ('9', '9'), ('12', '12'), ('1', '1'), ('8', '8'), ('10', '10'), ('11', '11'), ('6', '6'), ('5', '5')], max_length=2),
        ),
        migrations.AlterField(
            model_name='musicos',
            name='instrumento',
            field=models.CharField(choices=[('Piano', 'Piano'), ('Violin', 'Violin')], max_length=6),
        ),
        migrations.AlterField(
            model_name='ninjas',
            name='nivelMilitar',
            field=models.CharField(choices=[('Genin', 'Genin'), ('Anbu', 'Anbu'), ('Chunin', 'Chunin'), ('Sannin', 'Sannin'), ('Kage', 'Kage'), ('Jonin', 'Jonin')], max_length=6),
        ),
    ]
