# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.IntegerField()),
                ('latitud', models.IntegerField()),
                ('longitud', models.IntegerField()),
            ],
        ),
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
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('emp_id', models.AutoField(serialize=False, primary_key=True)),
                ('no_documento', models.CharField(unique=True, max_length=40)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('tipo_sangre', models.CharField(max_length=20, choices=[(b'O+', b'O+'), (b'O-', b'O-'), (b'A+', b'A+'), (b'A-', b'A-'), (b'B+', b'B+'), (b'B-', b'B-'), (b'AB+', b'AB+'), (b'AB-', b'AB-')])),
                ('experiencia', models.IntegerField()),
                ('jornada', models.CharField(default=b'Manana', max_length=15, choices=[(b'Manana', b'Ma\xc3\xb1ana'), (b'Tarde', b'Tarde'), (b'Noche', b'Noche')])),
                ('fecha_vinculacion', models.DateField(blank=True)),
                ('cargo', models.CharField(blank=True, max_length=150, null=True, choices=[(b'Vendedor', b'Vendedor'), (b'Jefe de taller', b'Jefe de taller'), (b'Gerente', b'Gerente'), (b'Mecanico', b'Mec\xc3\xa1nico')])),
                ('telefono', models.CharField(max_length=150)),
                ('genero', models.CharField(max_length=15, choices=[(b'Masculino', b'Masculino'), (b'Femenino', b'Femenino')])),
                ('fecha_nacimiento', models.DateField()),
                ('estado_empleado', models.BooleanField(default=True)),
            ],
            options={
                'permissions': (('listar_Empleados', 'Se permite editar, activar , desactivar'),),
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=100)),
                ('slug', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('costo', models.IntegerField(null=True, blank=True)),
                ('modelo_carro', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
                ('activo', models.BooleanField(default=True)),
                ('marca_carro', models.ForeignKey(blank=True, to='administrador.Marca', null=True)),
            ],
            options={
                'permissions': (('listar_Repuestos', 'Se permite editar, activar , desactivar'),),
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=100)),
                ('direccion', models.CharField(max_length=150)),
                ('telefono', models.TextField(max_length=150)),
                ('activo', models.BooleanField(default=True)),
                ('ciudad', models.ForeignKey(to='administrador.Ciudad')),
            ],
            options={
                'permissions': (('listar_Sucursales', 'Se permite editar, activar , desactivar'),),
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cilindraje', models.IntegerField()),
                ('linea', models.CharField(max_length=50)),
                ('modelo', models.IntegerField()),
                ('tipo_combustible', models.CharField(max_length=50, choices=[(b'Gasolina', b'Gasolina'), (b'Gas', b'Gas')])),
                ('color', models.CharField(max_length=50)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('empleado_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='administrador.Empleado')),
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('listar_Gerente', 'Se permite editar, activar , desactivar'), ('ver_reportes', 'permite ver los distintos reportes de la aplicacion')),
            },
            bases=('auth.user', 'administrador.empleado'),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='JefeTaller',
            fields=[
                ('empleado_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='administrador.Empleado')),
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('listar_Jefe_Taller', 'Se permite editar, activar , desactivar'),),
            },
            bases=('auth.user', 'administrador.empleado'),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SuperAdmin',
            fields=[
                ('empleado_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='administrador.Empleado')),
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('auth.user', 'administrador.empleado'),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='VehiculoNuevo',
            fields=[
                ('vehiculo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='administrador.Vehiculo')),
                ('valor', models.IntegerField()),
                ('codigo', models.CharField(max_length=10)),
                ('vendido', models.BooleanField(default=False)),
                ('fecha_ingreso', models.DateField(null=True, blank=True)),
            ],
            options={
                'permissions': (('listar_Vehiculo_Nuevo', 'Se permite editar, activar , desactivar'),),
            },
            bases=('administrador.vehiculo',),
        ),
        migrations.CreateModel(
            name='VehiculoUsado',
            fields=[
                ('vehiculo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='administrador.Vehiculo')),
                ('servicio', models.CharField(max_length=50, choices=[(b'Publico', b'Publico'), (b'Prviado', b'Privado')])),
                ('placa', models.CharField(unique=True, max_length=6)),
            ],
            options={
                'permissions': (('listar_Vehiculo_Usado', 'Se permite editar, activar , desactivar'),),
            },
            bases=('administrador.vehiculo',),
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('empleado_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='administrador.Empleado')),
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('listar_Vendedor', 'Se permite editar, activar , desactivar'),),
            },
            bases=('auth.user', 'administrador.empleado'),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='marca',
            field=models.ForeignKey(to='administrador.Marca', blank=True),
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='sucursal',
            field=models.ForeignKey(to='administrador.Sucursal', null=True),
        ),
        migrations.AddField(
            model_name='repuesto',
            name='sucursal',
            field=models.ForeignKey(to='administrador.Sucursal', null=True),
        ),
        migrations.AddField(
            model_name='empleado',
            name='jefe',
            field=models.ForeignKey(blank=True, to='administrador.Empleado', null=True),
        ),
        migrations.AddField(
            model_name='empleado',
            name='sucursal',
            field=models.ForeignKey(blank=True, to='administrador.Sucursal', null=True),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='departamento',
            field=models.ForeignKey(to='administrador.Departamento'),
        ),
        migrations.AlterUniqueTogether(
            name='repuesto',
            unique_together=set([('codigo', 'sucursal')]),
        ),
    ]
