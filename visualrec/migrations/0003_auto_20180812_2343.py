# Generated by Django 2.0.2 on 2018-08-12 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualrec', '0002_auto_20180724_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta_articulo',
            name='analisis',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='venta_articulo',
            name='analiticas',
            field=models.TextField(default=''),
        ),
    ]
