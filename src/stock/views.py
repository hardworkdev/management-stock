from django.shortcuts import render
from .models import *
from .forms import *
from django.urls import reverse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .functions import *
from django.contrib.auth.decorators import login_required
import datetime
from .context_processors import global_vars
# Create your views here.

def error_404_view(request, exception):
    context = {"name": "ThePythonDjango.com"}
    return render(request,'pages/error_404.html', context)


@login_required
def home(request):
    len_entree = len(Entree.objects.filter(deleted=False))
    len_sortie = len(Sortie.objects.filter(deleted=False))
    len_produit = len(Produit.objects.all())
    len_fourniseur = len(Fourniseur.objects.all())
    last_sortie = Sortie.objects.filter(deleted=False).order_by("-id")[:5]
    last_entree = Entree.objects.filter(deleted=False).order_by("-id")[:5]
    last_produit = Entree.objects.filter().order_by("-id")[:5]

    context = {"len_entree":len_entree, "len_sortie":len_sortie, "len_produit":len_produit, "len_fourniseur":len_fourniseur}
    context["last_sortie"] = last_sortie
    context["last_entree"] = last_entree
    context["last_produit"] = last_produit

    print("________________ ",global_vars(request))

    return render(request, 'pages/home.html', context)


@login_required
def fourniseur_list(request):
    fourniseurs = Fourniseur.objects.all()
    context = {"fourniseur_list": fourniseurs}

    return render(request, 'fourniseur/fourniseur_list.html', context)

@login_required
def create_fourniseur(request):
    context = {}
    form = FourniseurForm()
    if request.method == "POST":
        form = FourniseurForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(reverse('list_fourniseur'))

    print("@@@@@@@@@@@@@@@@@@@", form.errors)
    context["form"] = form


    return render(request, 'fourniseur/save.html',context)

@login_required
def update_fourniseur(request,pk):
    context = {}
    instance = get_object_or_404(Fourniseur, pk=pk)
    form = FourniseurForm(instance=instance)
    if request.method == "POST":
        form = FourniseurForm(request.POST ,instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('list_fourniseur'))

    context["form"] = form
    context["instance"] = instance


    return render(request, 'fourniseur/update.html',context)


@login_required
def list_produit(request,**kwargs):

    produits = Produit.objects.all().order_by("-pk")
    print(produits)
    context = {"produit_list": produits}
    print(kwargs)
    context["msg"] = request.GET.get('msg','')
    return render(request, 'produit/list_produit.html', context)

@login_required
def save_prduit(request):

    context = {}
    form = ProduitEntreeMultiForm()
    if request.method == "POST":
        form = ProduitEntreeMultiForm(request.POST or None)
        if form.is_valid():
            produit = form['produit'].save()
            entree = form['entree'].save(commit=False)
            entree.produit = produit
            entree.save()
            msg = calcule_stock(produit)
            return redirect(reverse('list_produit'))

    context["form"] = form


    return render(request, 'produit/save_produit.html',context)

@login_required
def update_produit(request,pk):
    context = {}
    
    instance = get_object_or_404(Produit, pk=pk)
    form = ProduitForm(instance=instance)
    if request.method == "POST":
        form = ProduitForm(request.POST ,instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('list_produit'))

    context["form"] = form
    context["instance"] = instance


    return render(request, 'produit/update_produit.html',context)

@login_required
def save_entree(request, pk):
    context = {}
    form = EntreeForm()
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == "POST":
        form = EntreeForm(request.POST or None)
        if form.is_valid():
            entree = form.save(commit=False)
            entree.produit = produit
            entree.save()
            msg = calcule_stock(produit)
            return redirect(reverse('list_produit'))

    context["form"] = form
    context["pk_produit"] = produit.pk


    return render(request, 'produit/save_entree.html',context)

from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def save_sortie(request, pk):
    context = {}
    form = SortieForm()
    produit = get_object_or_404(Produit, pk=pk)
    msg = None
    if request.method == "POST":
        form = SortieForm(request.POST or None)
        if form.is_valid():
            sortie = form.save(commit=False)
            msg = calcule_stock(produit, qt=sortie.qte_sortie)
            if msg is None:
                sortie.produit = produit
                sortie.save()
                calcule_stock(produit, qt=sortie.qte_sortie)
                return redirect(reverse('list_produit'))

    context["msg"] = msg
    context["form"] = form
    context["pk_produit"] = produit.pk


    return render(request, 'produit/save_sortie.html',context)

from django.utils.dateparse import parse_date

@login_required
def list_entree(request):
    
    fourniseur = request.POST.get('fournisseur','')
    fourniseur = int(fourniseur) if fourniseur else ''
    date = request.POST.get('date','')
    date= datetime.datetime.strptime(date, "%Y-%m-%d").date() if date else ''
    filter_params = {'deleted':False,}
    set_if_not_none(filter_params, 'fourniseur', fourniseur)
    set_if_not_none(filter_params, 'created_at__date', date)
    entrees = Entree.objects.filter(**filter_params).filter(sortie_avoir=None)
    fourniseur_list = Fourniseur.objects.all()
    context = {"entrees_list":entrees, "fourniseur_list":fourniseur_list,"fourniseur":fourniseur,"date":str(date)}
    return render(request, 'entree/list_entree.html', context)

@login_required
def update_entree(request, pk):
    
    instance = get_object_or_404(Entree, pk=pk)
    form = EntreeForm(instance=instance)
    if request.POST:
        form = EntreeForm(request.POST ,instance=instance)
        if form.is_valid():
            form = EntreeForm(request.POST, instance=instance)
            form.save()
            calcule_stock(instance.produit)
            return redirect(reverse("list_entree"))
    context = {'form':form, "instance":instance}
    return render(request, 'entree/update_entree.html', context)

@login_required
def deleted_entree(request, pk):

    instance = get_object_or_404(Entree,pk=pk)
    instance.deleted = True
    instance.save()
    avoir_sorties = AvoirSortie.objects.filter(entree=instance)
    for avoir in avoir_sorties:
        avoir.entree= None
        avoir.save()
    calcule_stock(instance.produit)
    return redirect(reverse("list_entree"))

@login_required
def deleted_sortie(request, pk):

    instance = get_object_or_404(Sortie,pk=pk)
    instance.deleted = True
    instance.save()
    calcule_stock(instance.produit)
    return redirect(reverse("list_sortie"))

@login_required
def list_sortie(request):
    date = request.POST.get('date','')
    date= datetime.datetime.strptime(date, "%Y-%m-%d").date() if date else ''
    client = request.POST.get('client','')
    client = int(client) if client else '' 
    filter_params = {"deleted":False}
    set_if_not_none(filter_params, 'date_sortie', date)
    set_if_not_none(filter_params, 'client', client)
    sorties = Sortie.objects.filter(**filter_params) 
    list_client = Client.objects.all()
    context = {"sortie_list":sorties, "list_client":list_client, "client":client, "date":str(date)}
    return render(request, 'sortie/list_sortie.html', context)

@login_required
def update_sortie(request, pk):
    
    instance = get_object_or_404(Sortie, pk=pk)
    form = SortieForm(instance=instance)
    if request.POST:
        form = SortieForm(request.POST, instance=instance)
        form.save()
        calcule_stock(instance.produit)
        return redirect(reverse("list_sortie"))
    context = {'form':form, "instance":instance}
    return render(request, 'sortie/update_sortie.html', context)


@login_required
def list_marque(request):

    list_marque = Marque.objects.all()

    form = MarqueForm()

    if request.POST:
        form = MarqueForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(reverse("list_marque"))
    
    context = {"form":form, "list_marque":list_marque}

    return render(request, 'marque/form_create_marque.html', context)

@login_required
def detail_marque(request, pk):
    list_marque = Marque.objects.all()
    instance = get_object_or_404(Marque, pk=pk)
    form = MarqueForm(instance=instance)

    if request.POST:
        form = MarqueForm(request.POST , instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse("list_marque"))
    
    context = {"form":form, "list_marque":list_marque,"instance":instance}

    return render(request, 'marque/form_update_marque.html', context)

@login_required
def list_category(request):

    list_category = Category.objects.all()

    form = MarqueForm()

    if request.POST:
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(reverse("list_category"))
    
    context = {"form":form, "list_category":list_category}

    return render(request, 'category/form_create_category.html', context)

@login_required
def detail_category(request, pk):
    list_category = Category.objects.all()
    instance = get_object_or_404(Category, pk=pk)
    form = CategoryForm(instance=instance)

    if request.POST:
        form = CategoryForm(request.POST , instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse("list_category"))
    
    context = {"form":form, "list_category":list_category,"instance":instance}

    return render(request, 'category/form_update_category.html', context)


@login_required 
def list_client(request):
    client = Client.objects.all()

    context = {"list_client":client}

    return render(request, 'client/list_client.html', context)



@login_required 
def save_client(request):
    context = {}
    form = ClientForm()
    if request.POST:
        form = ClientForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(reverse('list_client'))
    context["form"] = form

    return render(request, 'client/create_client.html', context)




def update_client(request, pk):
    context = {}
    instance = get_object_or_404(Client, pk=pk)
    form = ClientForm(instance=instance)
    if request.POST:
        form = ClientForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('list_client'))
    context["form"] = form
    context["instance"] = instance

    return render(request, 'client/update_client.html', context)




def list_avoir_entree(request):
    client = request.POST.get('client','')
    client = int(client) if client else ''
    date = request.POST.get('date','')
    date = datetime.datetime.strptime(date, "%Y-%m-%d").date() if date else ''
    filter_params = {'deleted':False}
    set_if_not_none(filter_params, 'sortie__client__pk', client)
    set_if_not_none(filter_params, 'created_at__date', date)
    client_list = Client.objects.all()
    avoirs = AvoirEntree.objects.filter(**filter_params)
    context = {"client_list":client_list,"avoirs":avoirs, "client":client ,"date":date}
    return render(request, "avoir/list_avoir_entree.html",context)


def save_avoir_entree(request, pk_sortie):
    context = {}
    form = EntreeAvoirForm()
    sortie = get_object_or_404(Sortie, pk=pk_sortie)
    if request.POST:
        print("i am here now ___________________")

        form = EntreeAvoirForm(request.POST or None)
        avoirs = AvoirEntree.objects.filter(sortie=sortie)
        total_avoir_entree = sum([avoir.qte_entree for avoir in avoirs])
        if form.is_valid():
            avoir_entree = form.save(commit=False)
            if total_avoir_entree + avoir_entree.qte_entree <= sortie.qte_sortie:
                avoir_entree.sortie = sortie
                avoir_entree.save()
                calcule_stock(sortie.produit)
                return redirect(reverse('list_avoir_entree_url'))
            else: # for error quantite avoir
                context["form"] = form
                context["sortie_pk"] = sortie.pk
                context["smg_qte_avoir"] = "Error Quantite"
                return render(request, 'avoir/save_avoir_entree.html',context)
    
    context["form"] = form
    context["sortie_pk"] = sortie.pk
    return render(request, 'avoir/save_avoir_entree.html',context)





def list_avoir_sortie(request):
    fourniseur = request.POST.get('fourniseur','')
    fourniseur = int(fourniseur) if fourniseur else ''

    entree = request.POST.get('entree','')
    entree = int(entree) if entree else ''  
    print(entree,"what is this maan ________________________________")


    date = request.POST.get('date','')
    date = datetime.datetime.strptime(date, "%Y-%m-%d").date() if date else ''
    filter_params = {'deleted':False}
    set_if_not_none(filter_params, 'entree__fourniseur__pk', fourniseur)
    set_if_not_none(filter_params, 'created_at__date', date)
    set_if_not_none(filter_params, 'entree__pk', entree)
    fourniseur_list = Fourniseur.objects.all()
    avoirs = AvoirSortie.objects.filter(**filter_params)
    context = {"fourniseur_list":fourniseur_list,"avoirs":avoirs,"fourniseur":fourniseur,"date":str(date)}
    return render(request, "avoir/list_avoir_sortie.html",context)


def save_avoir_sortie(request, pk_entree):
    context = {}
    form = SortieAvoirForm()
    entree = get_object_or_404(Entree, pk=pk_entree)
    if request.POST:
        print("i am here now ___________________")

        form = SortieAvoirForm(request.POST or None)
        avoirs = AvoirSortie.objects.filter(entree=entree)
        total_avoir_sortie = sum([avoir.qte_sortie for avoir in avoirs])
        if form.is_valid():
            avoir_sortie = form.save(commit=False)
            if total_avoir_sortie + avoir_sortie.qte_sortie <= entree.qte_entree:
                avoir_sortie.entree = entree
                avoir_sortie.save()
                calcule_stock(entree.produit)
                return redirect(reverse('list_avoir_sortie_url'))
            else: # for error quantite avoir
                context["form"] = form
                context["entree_pk"] = entree.pk
                context["smg_qte_avoir"] = "Error Quantite"
                return render(request, 'avoir/save_avoir_sortie.html',context)
    
    context["form"] = form
    context["entree_pk"] = entree.pk
    return render(request, 'avoir/save_avoir_sortie.html',context)


