# Generated by Django 4.0.6 on 2022-07-19 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='owner',
            field=models.CharField(default='None', max_length=100),
            preserve_default=False,
        ),
    ]
