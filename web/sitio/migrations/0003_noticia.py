# Generated by Django 4.1.2 on 2022-11-14 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0002_remove_cliente_id_cliente_direccion_cliente_mobile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('imagen', models.ImageField(upload_to='sitio/static/media')),
                ('titular', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('previsualizacion', models.CharField(max_length=150)),
                ('cuerpo', models.CharField(max_length=500)),
                ('fecha', models.DateTimeField(verbose_name='Noticia a '))
            ],
        ),
    ]
