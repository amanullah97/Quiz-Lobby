# Generated by Django 2.2.7 on 2021-02-26 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20210223_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='figure',
        ),
    ]