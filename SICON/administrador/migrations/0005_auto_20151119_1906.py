# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0004_auto_20151107_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.IntegerField()),
                ('latitud', models.IntegerField()),
                ('longitud', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='ciudad',
            name='departamento_id',
            field=models.ForeignKey(to='administrador.Departamento'),
        ),
    ]
