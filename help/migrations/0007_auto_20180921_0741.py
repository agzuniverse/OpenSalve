# Generated by Django 2.1.1 on 2018-09-21 07:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_users_role'),
        ('help', '0006_auto_20180916_0711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(help_text='Unique ID of comment', primary_key=True, serialize=False)),
                ('comment', models.CharField(help_text='Comment text', max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to='accounts.Users')),
            ],
        ),
        migrations.AddField(
            model_name='requests',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]