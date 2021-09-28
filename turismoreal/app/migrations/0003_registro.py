# Generated by Django 2.2.3 on 2021-09-22 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210921_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_registro', models.IntegerField(choices=[[0, 'consultas'], [1, 'reclamos'], [2, 'sugerencias'], [3, 'felicitaciones'], [4, 'registrarme']])),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
    ]
