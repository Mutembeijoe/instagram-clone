# Generated by Django 2.2.7 on 2019-11-17 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='comment',
        ),
    ]
