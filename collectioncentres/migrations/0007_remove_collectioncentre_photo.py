# Generated by Django 2.1.2 on 2018-12-12 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collectioncentres', '0006_auto_20181212_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collectioncentre',
            name='photo',
        ),
    ]
