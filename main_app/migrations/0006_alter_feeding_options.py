# Generated by Django 4.0.6 on 2022-07-22 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_cat_toys'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feeding',
            options={'ordering': ['-date']},
        ),
    ]