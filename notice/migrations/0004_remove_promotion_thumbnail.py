# Generated by Django 4.2.5 on 2023-09-28 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0003_alter_promotion_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promotion',
            name='thumbnail',
        ),
    ]
