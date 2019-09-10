# Generated by Django 2.2.4 on 2019-08-26 22:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Fourniseur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=50)),
                ('tele', models.CharField(max_length=10)),
                ('fix', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('date_create', models.DateTimeField(default=datetime.datetime(2019, 8, 27, 0, 19, 9, 49940))),
            ],
        ),
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('prix_achat', models.FloatField(max_length=100)),
                ('qte_stock', models.IntegerField(default=0)),
                ('qte_stock_min', models.IntegerField(default=0)),
                ('date_create', models.DateTimeField(default=datetime.datetime.now)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.Category')),
                ('marque', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.Marque')),
            ],
        ),
        migrations.CreateModel(
            name='Sortie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sortie', models.DateField(default=datetime.datetime.now)),
                ('qte_sortie', models.IntegerField(default=0)),
                ('produit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.Produit')),
            ],
        ),
        migrations.CreateModel(
            name='Entree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qte_entree', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('fourniseur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.Fourniseur')),
                ('produit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.Produit')),
            ],
        ),
    ]
