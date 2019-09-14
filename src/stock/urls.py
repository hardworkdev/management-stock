from django.urls import path
from .views import *


urlpatterns = [

    path('', home, name="home"),
    path('fourniseur', fourniseur_list , name="list_fourniseur"),
    path('fourniseur/create', create_fourniseur , name="create_fourniseur"),
    path('fourniseur/<int:pk>/update', update_fourniseur , name="update_fourniseur"),
    path('produit', list_produit , name="list_produit"),
    path('produit/create', save_prduit , name="save_produit"),
    path('produit/<int:pk>/update', update_produit , name="update_produit"),
    path('produit/entree/<int:pk>/create', save_entree , name="save_entree"),
    path('produit/sortie/<int:pk>/create', save_sortie , name="save_sortie"),
    path('entree', list_entree , name="list_entree"),
    path('entree/<int:pk>/update', update_entree , name="update_entree"),
    path('sortie', list_sortie , name="list_sortie"),
    path('sortie/<int:pk>/update', update_sortie , name="update_sortie"),
    path('entree/<int:pk>/deleted', deleted_entree , name="deleted_entree"),
    path('sortie/<int:pk>/deleted', deleted_sortie , name="deleted_sortie"),
    path('marque', list_marque , name="list_marque"), 
    path('category', list_category , name="list_category"), 
    path('marque/<int:pk>/detail', detail_marque , name="detail_marque"), 
    path('category/<int:pk>/detail', detail_category , name="detail_category"), 
    path('client', list_client , name="list_client"), 
    path('client/create', save_client , name="save_client"), 
    path('client/<int:pk>/update', update_client , name="update_client"), 
    path('retour/sortie/<int:pk_sortie>/create', save_avoir_entree , name="save_avoir_entree"), 
    path('retour/entree', list_avoir_sortie , name="list_avoir_sortie_url"), 
    path('retour/sortie', list_avoir_entree , name="list_avoir_entree_url"), 
    path('retour/entree/<int:pk_entree>/create', save_avoir_sortie , name="save_avoir_sortie"), 

]