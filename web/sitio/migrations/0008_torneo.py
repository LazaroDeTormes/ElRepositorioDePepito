# Generated by Django 4.1.2 on 2022-11-18 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0007_alter_noticia_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('titulo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
                ('requisitos', models.CharField(max_length=100)),
            ],
        ),
    ]