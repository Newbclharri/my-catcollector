# Generated by Django 4.0.6 on 2022-07-24 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_cat_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='owner',
        ),
    ]
