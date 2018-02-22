# Generated by Django 2.0.1 on 2018-02-22 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0009_auto_20180222_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='en_name',
            field=models.CharField(blank=True, max_length=140, verbose_name='Nombre español'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='brands/cat/', verbose_name='Imágen principal'),
        ),
    ]
