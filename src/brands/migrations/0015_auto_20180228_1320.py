# Generated by Django 2.0.1 on 2018-02-28 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0014_auto_20180228_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='en_name',
            field=models.CharField(blank=True, max_length=140, verbose_name='Nombre inglés'),
        ),
        migrations.AlterField(
            model_name='department',
            name='es_name',
            field=models.CharField(blank=True, max_length=140, verbose_name='Nombre español'),
        ),
    ]
