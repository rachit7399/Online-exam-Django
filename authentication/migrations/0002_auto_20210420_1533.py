# Generated by Django 3.0.8 on 2021-04-20 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='demo_first_name', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='demo_last_name', max_length=255),
        ),
    ]
