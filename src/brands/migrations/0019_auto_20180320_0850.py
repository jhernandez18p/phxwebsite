# Generated by Django 2.0.1 on 2018-03-20 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0018_auto_20180319_2141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['-es_name', '-en_name'], 'verbose_name': 'Marca', 'verbose_name_plural': 'Marcas'},
        ),
    ]