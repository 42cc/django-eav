# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eav', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False),
        ),
        migrations.AlterField(
            model_name='value',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created'),
        ),
    ]
