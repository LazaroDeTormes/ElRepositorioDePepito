# Generated by Django 4.1.2 on 2022-11-14 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0003_noticia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(upload_to='sitio/static/media'),
        ),
    ]