# Generated by Django 4.2.5 on 2023-09-29 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0007_promotion_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promotion',
            name='thumbnail',
        ),
    ]
