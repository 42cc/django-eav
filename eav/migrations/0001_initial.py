# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager
import datetime
import eav.fields
import django.contrib.sites.managers


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='User-friendly attribute name', max_length=100, verbose_name='name')),
                ('slug', eav.fields.EavSlugField(help_text='Short unique attribute label', verbose_name='slug')),
                ('description', models.CharField(help_text='Short description', max_length=256, null=True, verbose_name='description', blank=True)),
                ('type', models.CharField(max_length=20, null=True, verbose_name='type', blank=True)),
                ('datatype', eav.fields.EavDatatypeField(max_length=6, verbose_name='data type', choices=[(b'text', 'Text'), (b'float', 'Float'), (b'int', 'Integer'), (b'date', 'Date'), (b'bool', 'True / False'), (b'object', 'Django Object'), (b'enum', 'Multiple Choice')])),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='created', editable=False)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('required', models.BooleanField(default=False, verbose_name='required')),
            ],
            options={
                'ordering': ['name'],
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='EnumGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='EnumValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(unique=True, max_length=50, verbose_name='value', db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entity_id', models.IntegerField()),
                ('value_text', models.TextField(null=True, blank=True)),
                ('value_float', models.FloatField(null=True, blank=True)),
                ('value_int', models.IntegerField(null=True, blank=True)),
                ('value_date', models.DateTimeField(null=True, blank=True)),
                ('value_bool', models.NullBooleanField()),
                ('generic_value_id', models.IntegerField(null=True, blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('attribute', models.ForeignKey(verbose_name='attribute', to='eav.Attribute')),
                ('entity_ct', models.ForeignKey(related_name='value_entities', to='contenttypes.ContentType')),
                ('generic_value_ct', models.ForeignKey(related_name='value_values', blank=True, to='contenttypes.ContentType', null=True)),
                ('value_enum', models.ForeignKey(related_name='eav_values', blank=True, to='eav.EnumValue', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='enumgroup',
            name='enums',
            field=models.ManyToManyField(to='eav.EnumValue', verbose_name='enum group'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='enum_group',
            field=models.ForeignKey(verbose_name='choice group', blank=True, to='eav.EnumGroup', null=True),
        ),
        migrations.AddField(
            model_name='attribute',
            name='site',
            field=models.ForeignKey(default=1, verbose_name='site', to='sites.Site'),
        ),
        migrations.AlterUniqueTogether(
            name='attribute',
            unique_together=set([('site', 'slug')]),
        ),
    ]
