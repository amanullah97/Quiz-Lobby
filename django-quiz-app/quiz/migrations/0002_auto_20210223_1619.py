# Generated by Django 2.2.7 on 2021-02-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='course_rel',
        ),
        migrations.AddField(
            model_name='quiz',
            name='course_rel',
            field=models.ManyToManyField(to='quiz.Course'),
        ),
    ]
