# Generated by Django 2.2.3 on 2021-10-14 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211014_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='id',
            field=models.AutoField(max_length=15, primary_key=True, serialize=False, unique=True),
        ),
    ]