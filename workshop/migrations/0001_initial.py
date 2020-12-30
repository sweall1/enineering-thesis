# Generated by Django 2.0.13 on 2020-11-27 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City', models.CharField(max_length=200, null=True)),
                ('StreetName', models.CharField(max_length=200, null=True)),
                ('ZipCode', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Diagnostyka', 'Diagnostyka'), ('Naprawy mechaniczne', 'Naprawy mechaniczne'), ('Naprawy blacharsko lakiernicze', 'Naprawy blacharsko lakiernicze'), ('Wulkanizacja', 'Wulkanizacja'), ('Detailing', 'Detailing')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fault',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, null=True)),
                ('phone', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.FloatField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('brands', models.CharField(max_length=200, null=True)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workshop.Address')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workshop.Category')),
                ('fault', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workshop.Fault')),
                ('note', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workshop.Note')),
            ],
        ),
    ]
