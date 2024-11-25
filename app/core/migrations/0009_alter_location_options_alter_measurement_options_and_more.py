# Generated by Django 5.1.2 on 2024-11-25 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_measurement_sensor_alter_sensor_location_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['name'], 'verbose_name': 'Location', 'verbose_name_plural': 'Locations'},
        ),
        migrations.AlterModelOptions(
            name='measurement',
            options={'ordering': ['timestamp'], 'verbose_name': 'Measurement', 'verbose_name_plural': 'Measurements'},
        ),
        migrations.AlterModelOptions(
            name='sensor',
            options={'ordering': ['name'], 'verbose_name': 'Sensor', 'verbose_name_plural': 'Sensors'},
        ),
        migrations.AlterModelOptions(
            name='sensortype',
            options={'ordering': ['name'], 'verbose_name': 'Sensor Type', 'verbose_name_plural': 'Sensor Types'},
        ),
    ]
