# Generated by Django 2.2.4 on 2019-09-06 21:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0013_auto_20190906_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 6, 23, 14, 8, 459125), null=True),
        ),
        migrations.AlterField(
            model_name='fourniseur',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 6, 23, 14, 8, 448156), null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 6, 23, 14, 8, 458129), null=True),
        ),
        migrations.AlterField(
            model_name='sortie',
            name='date_sortie',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 6, 23, 14, 8, 458129), null=True),
        ),
    ]
