# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 21:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_patient_classification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queuedpatient',
            name='patient',
        ),
        migrations.DeleteModel(
            name='QueuedPatient',
        ),
    ]
