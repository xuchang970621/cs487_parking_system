# Generated by Django 2.2.5 on 2020-04-27 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0002_parkingspot_booked_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parkingspot',
            options={'permissions': (('booked', 'This parking spot is booked by this user'),)},
        ),
    ]