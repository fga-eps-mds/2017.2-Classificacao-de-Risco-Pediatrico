# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20171101_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age_range',
            field=models.IntegerField(blank=True, choices=[(0, 'Faixa etária indefinida'), (1, '0 até 28 dias'), (2, '29 dias à 3 meses'), (3, '3 meses à 2 anos'), (4, '2 anos à 10 anos'), (5, 'Acima de 10 anos')], default=0, verbose_name='Classification'),
        ),
    ]
