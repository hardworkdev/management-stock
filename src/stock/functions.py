from .models import Entree, Sortie , AvoirEntree, AvoirSortie

# def calcule_stock(produit, qt=0):
#     message = None
    
#     if produit.qte_stock - qt >= 0:
#         qte_entree_produit = [entree.qte_entree for entree in Entree.objects.filter(deleted=False, produit=produit)]
#         qte_sortie_produit = [sortie.qte_sortie for sortie in Sortie.objects.filter(deleted=False, produit=produit)]
#         quantitier = sum(qte_entree_produit) - sum(qte_sortie_produit)
#         produit.qte_stock = quantitier
#         produit.save()
#     else:
#         msg_str = "Vous avez depasser la quantitée de la produit "+ str(produit.ref) +" / " + str(produit.designation)
#         message = msg_str 
#     return message


def set_if_not_none(mapping, key, value):
    if value is not '':
        mapping[key] = value

    

def calcule_stock(produit, qt=0):
    message = None
    
    if produit.qte_stock - qt >= 0:
        qte_entree_produit = [entree.qte_entree for entree in Entree.objects.filter(deleted=False, produit=produit)]
        qte_entree_avoir_produit = [entree.qte_entree for entree in AvoirEntree.objects.filter(deleted=False, sortie__produit=produit)]
        qte_sortie_produit = [sortie.qte_sortie for sortie in Sortie.objects.filter(deleted=False, produit=produit)]
        qte_sortie_avoir_produit = [sortie.qte_sortie for sortie in AvoirSortie.objects.filter(deleted=False, entree__produit=produit)]
        quantitier =( sum(qte_entree_produit) + sum(qte_entree_avoir_produit) ) - (sum(qte_sortie_produit) + sum(qte_sortie_avoir_produit) )
        produit.qte_stock = quantitier
        produit.save()
    else:
        msg_str = "Vous avez depasser la quantitée de la produit "+ str(produit.ref) +" / " + str(produit.designation)
        message = msg_str 
    return message