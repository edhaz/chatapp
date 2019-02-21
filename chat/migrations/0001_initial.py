# Generated by Django 2.1.7 on 2019-02-21 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chatter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_joined', models.DateTimeField(verbose_name='date joined')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=140)),
                ('votes', models.IntegerField(default=0)),
                ('chatter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Chatter')),
            ],
        ),
    ]