# Generated by Django 2.1 on 2018-10-05 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textmessage',
            name='talktime',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]