# Generated by Django 4.2 on 2023-04-19 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_foto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]
