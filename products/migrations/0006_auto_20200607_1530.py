# Generated by Django 3.0.7 on 2020-06-07 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200607_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='dimension',
            name='d',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='dimension',
            name='l',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='dimension',
            name='h',
            field=models.FloatField(default=0.0),
        ),
    ]
