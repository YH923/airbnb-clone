# Generated by Django 3.0.2 on 2020-02-04 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_auto_20200204_1203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amenity',
            options={'verbose_name_plural': 'Amenities'},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'verbose_name_plural': 'Facilities'},
        ),
        migrations.AlterModelOptions(
            name='houserule',
            options={'verbose_name_plural': 'HouseRule'},
        ),
    ]