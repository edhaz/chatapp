# Generated by Django 2.1.7 on 2019-02-21 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatter',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
