# Generated by Django 3.0.2 on 2020-02-04 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_room_newone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='newone',
        ),
    ]
