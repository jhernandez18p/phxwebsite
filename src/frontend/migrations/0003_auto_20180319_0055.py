# Generated by Django 2.0.1 on 2018-03-19 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20180222_1055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timeline',
            options={'verbose_name': 'Linea de tiempo', 'verbose_name_plural': 'Linea de tiempo'},
        ),
        migrations.AlterField(
            model_name='timeline',
            name='Company',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontend.Company'),
        ),
    ]
