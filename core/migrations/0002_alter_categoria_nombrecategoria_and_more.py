# Generated by Django 4.0.5 on 2022-06-12 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombreCategoria',
            field=models.CharField(max_length=50, verbose_name='nombreCategoria'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_producto',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id_producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre_producto',
            field=models.CharField(max_length=50, verbose_name='nombre_producto'),
        ),
    ]