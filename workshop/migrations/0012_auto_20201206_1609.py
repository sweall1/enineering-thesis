# Generated by Django 2.0.13 on 2020-12-06 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0011_auto_20201201_2057'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fault',
            new_name='Task',
        ),
        migrations.AddField(
            model_name='workshop',
            name='Task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workshop.Task'),
        ),
    ]