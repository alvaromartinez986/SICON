# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=40)),
                ('nombre', models.CharField(unique=True, max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('costo', models.IntegerField()),
                ('marca_carro', models.CharField(max_length=40)),
                ('modelo_carro', models.CharField(max_length=40)),
                ('cantidad', models.IntegerField()),
            ],
        ),
    ]
