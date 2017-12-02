# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_rating', '0002_machinelearning_10ymore_machinelearning_28d_machinelearning_29d_2m_machinelearning_2m_3y_machinelear'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinelearning_10ymore',
            name='classification',
            field=models.IntegerField(choices=[(1, 'Atendimento Imediato'), (2, 'Atendimento Hospitalar'), (3, 'Atendimento Ambulatorial')], default=0, verbose_name='Classification'),
        ),
        migrations.AddField(
            model_name='machinelearning_28d',
            name='classification',
            field=models.IntegerField(choices=[(1, 'Atendimento Imediato'), (2, 'Atendimento Hospitalar'), (3, 'Atendimento Ambulatorial')], default=0, verbose_name='Classification'),
        ),
        migrations.AddField(
            model_name='machinelearning_29d_2m',
            name='classification',
            field=models.IntegerField(choices=[(1, 'Atendimento Imediato'), (2, 'Atendimento Hospitalar'), (3, 'Atendimento Ambulatorial')], default=0, verbose_name='Classification'),
        ),
        migrations.AddField(
            model_name='machinelearning_2m_3y',
            name='classification',
            field=models.IntegerField(choices=[(1, 'Atendimento Imediato'), (2, 'Atendimento Hospitalar'), (3, 'Atendimento Ambulatorial')], default=0, verbose_name='Classification'),
        ),
        migrations.AddField(
            model_name='machinelearning_3y_10y',
            name='classification',
            field=models.IntegerField(choices=[(1, 'Atendimento Imediato'), (2, 'Atendimento Hospitalar'), (3, 'Atendimento Ambulatorial')], default=0, verbose_name='Classification'),
        ),
    ]
