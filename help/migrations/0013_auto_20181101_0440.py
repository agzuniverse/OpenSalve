# Generated by Django 2.1.2 on 2018-11-01 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0012_requests_need_water'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requests',
            old_name='need_food',
            new_name='need_first_aid',
        ),
        migrations.RenameField(
            model_name='requests',
            old_name='need_water',
            new_name='need_food_water',
        ),
        migrations.RenameField(
            model_name='requests',
            old_name='need_medicine',
            new_name='need_medical',
        ),
        migrations.AddField(
            model_name='requests',
            name='desc',
            field=models.CharField(blank=True, help_text='Further description', max_length=200),
        ),
        migrations.AddField(
            model_name='requests',
            name='need_transport',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='requests',
            name='status',
            field=models.CharField(blank=True, help_text='Status of request', max_length=50),
        ),
    ]
