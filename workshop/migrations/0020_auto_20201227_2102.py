# Generated by Django 2.0.13 on 2020-12-27 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0019_auto_20201213_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='Price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workshop',
            name='Quality',
            field=models.IntegerField(null=True),
        ),
    ]
