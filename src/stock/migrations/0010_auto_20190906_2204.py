# Generated by Django 2.2.4 on 2019-09-06 20:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0009_auto_20190831_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=50)),
                ('tele', models.CharField(max_length=10, unique=True)),
                ('fix', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 6, 22, 4, 9, 825060), null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='fourniseur',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 6, 22, 4, 9, 812099), null=True),
        ),
        migrations.AlterField(
            model_name='fourniseur',
            name='nom',
            field=models.CharField(max_length=20, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 6, 22, 4, 9, 824064), null=True),
        ),
    ]