# Generated by Django 3.0.6 on 2020-05-27 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20200527_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='color',
            field=models.CharField(default='Black', max_length=20),
        ),
    ]
