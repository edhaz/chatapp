# Generated by Django 2.1.7 on 2019-02-21 12:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20190221_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='posted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]