# Generated by Django 2.1.2 on 2018-12-12 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectioncentres', '0005_collectioncentre_supplies'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectioncentre',
            name='incharge',
            field=models.CharField(default='Subin', help_text='Camp incharge', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collectioncentre',
            name='phone',
            field=models.CharField(default='9874563210', help_text='Camp phone number', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collectioncentre',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='camps/%Y/%m/%d/'),
        ),
    ]
