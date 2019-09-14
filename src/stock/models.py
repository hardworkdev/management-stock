from django.db import models
import datetime
from django.contrib.auth.models import User


class Marque(models.Model):
    nom = models.CharField(max_length=20)
    def __str__(self):
        return self.nom


class Category(models.Model):
    nom = models.CharField(max_length=20)
    def __str__(self):
        return self.nom


class Fourniseur(models.Model):
    nom = models.CharField(max_length=20, verbose_name="Nom")
    prenom = models.CharField(max_length=20)
    adresse = models.CharField(max_length=50)
    tele = models.CharField(max_length=10, unique=True)
    fix = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True)
    def __str__(self):
        return self.nom + "  " + self.prenom
    

class Produit(models.Model):
    ref = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    prix_achat = models.FloatField(max_length=100)
    qte_stock = models.PositiveIntegerField(default=0)
    qte_stock_min = models.PositiveIntegerField(default=0)
    marque = models.ForeignKey(Marque, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL , null=True )
    date_create = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
       return self.ref



class Entree(models.Model):

    created_at = models.DateTimeField(default=datetime.datetime.now)
    qte_entree = models.PositiveIntegerField(default=0)
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, null=True)
    fourniseur = models.ForeignKey(Fourniseur, on_delete=models.SET_NULL, null=True)
    sortie_avoir = models.ForeignKey('Sortie', on_delete=models.SET_NULL, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return "ID : "+ str(self.pk)

class Sortie(models.Model):

    date_sortie = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True)
    qte_sortie = models.PositiveIntegerField(default=0)
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, null=True)
    deleted = models.BooleanField(default=False)
    entree_avoir = models.ForeignKey('Entree', on_delete=models.SET_NULL, null=True, blank=True)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Sortie "+ str(self.id)




class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    adresse = models.CharField(max_length=50, null=True, blank=True)
    tele = models.CharField(max_length=10, unique=True, blank=True)
    email = models.EmailField(null=True)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True)

    def __str__(self):
        return self.nom+"   "+self.prenom

    
class Client(models.Model):
    nom = models.CharField(max_length=20, verbose_name="Nom")
    prenom = models.CharField(max_length=20)
    tele = models.CharField(max_length=10, unique=True)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True)

    def __str__(self):
        return self.nom +"  "+ self.prenom
    

class AvoirEntree(models.Model):
    qte_entree = models.PositiveIntegerField(default=0)
    sortie = models.ForeignKey('Sortie', on_delete=models.SET_NULL, null=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return "Entree Avoir "+ str(self.id)

class AvoirSortie(models.Model):

    qte_sortie = models.PositiveIntegerField(default=0)
    entree = models.ForeignKey('Entree', on_delete=models.SET_NULL, null=True, blank=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True)

    def __str__(self):
        return "Sortie Avoir "+ str(self.id)