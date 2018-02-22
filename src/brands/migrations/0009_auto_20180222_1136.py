# Generated by Django 2.0.1 on 2018-02-22 16:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0008_auto_20180222_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='uploaded_at',
        ),
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Creado'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='brands/cat/', verbose_name='Imágen principal'),
        ),
    ]
