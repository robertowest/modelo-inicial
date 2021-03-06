# Generated by Django 3.1.3 on 2021-09-20 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diccionario', '0002_auto_20210920_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('tipo_calle', models.CharField(choices=[('avda', 'Avenida'), ('barrio', 'Barrio'), ('calle', 'Calle'), ('pje', 'Pasaje'), ('ruta', 'Ruta')], default='calle', max_length=6)),
                ('nombre', models.CharField(blank=True, max_length=80, null=True)),
                ('numero', models.IntegerField(blank=True, null=True, verbose_name='Número')),
                ('piso', models.CharField(blank=True, max_length=2, null=True)),
                ('puerta', models.CharField(blank=True, max_length=2, null=True)),
                ('barrio', models.CharField(blank=True, max_length=40, null=True)),
                ('provincia_texto', models.CharField(blank=True, max_length=50, null=True)),
                ('departamento_texto', models.CharField(blank=True, max_length=50, null=True)),
                ('localidad_texto', models.CharField(blank=True, max_length=50, null=True)),
                ('observacion_texto', models.TextField(blank=True, null=True, verbose_name='Nota')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domicilio_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domicilio_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modificado por')),
                ('tipo', models.ForeignKey(blank=True, default=1, limit_choices_to={'active': True, 'tabla': 'domicilio'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='diccionario.diccionario')),
            ],
            options={
                'verbose_name': 'Domicilio',
                'verbose_name_plural': 'Domicilios',
                'db_table': 'domicilio',
            },
        ),
    ]
