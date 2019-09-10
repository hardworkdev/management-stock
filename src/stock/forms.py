from django.forms import ModelForm
from django import forms
from .models import *

class FourniseurForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(FourniseurForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Fourniseur
        exclude = ('created_at',)


class ProduitForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProduitForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Produit
        exclude = ('qte_stock','date_create')

class EntreeForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(EntreeForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Entree
        exclude = ('produit','deleted','sortie_avoir')


class SortieForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(SortieForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Sortie
        exclude = ('produit','deleted','entree_avoir')



from betterforms.multiform import MultiModelForm
from betterforms.multiform import MultiForm
from collections import OrderedDict

class ProduitEntreeMultiForm(MultiModelForm):
    # def __init__(self, *args, **kwargs):
    #     self.instances = kwargs.pop('instance', None)
    #     if self.instances is None:
    #         self.instances = {}
    #     super(ProduitEntreeMultiForm, self).__init__(*args, **kwargs)



    form_classes = OrderedDict(
        (('produit', ProduitForm),
        ('entree', EntreeForm),)
    )



class MarqueForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MarqueForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Marque
        fields = '__all__'




class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Category
        fields = '__all__'
    

class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Client
        exclude = ('created_at',)



class EntreeAvoirForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(EntreeAvoirForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Entree
        exclude = ('produit','deleted','sortie_avoir', 'fourniseur')

    

class SortieAvoirForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(SortieAvoirForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Sortie
        exclude = ('produit','deleted','client', 'entree_avoir' )