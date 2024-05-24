# Generated by Django 5.0.4 on 2024-05-21 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0004_alter_trajectories_taxi_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trajectories',
            name='date',
            field=models.DateTimeField(verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='trajectories',
            name='taxi_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxi.taxi'),
        ),
    ]