# Generated by Django 5.0.4 on 2024-05-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0003_alter_trajectories_date_alter_trajectories_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trajectories',
            name='taxi_id',
            field=models.IntegerField(verbose_name='taxi_id'),
        ),
    ]
