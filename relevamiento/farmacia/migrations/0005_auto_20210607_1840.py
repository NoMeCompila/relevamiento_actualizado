# Generated by Django 3.2.2 on 2021-06-07 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0004_programa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='baja',
        ),
        migrations.AddField(
            model_name='programa',
            name='estado',
            field=models.BooleanField(default=False, verbose_name='Programa dado de baja'),
        ),
        migrations.AddField(
            model_name='provincia',
            name='estado',
            field=models.BooleanField(default=False, verbose_name='Provincia activa (con farmacias)'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='usuario dado de baja si/no'),
        ),
    ]
