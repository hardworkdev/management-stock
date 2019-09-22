from django import template
from stock.models import AvoirSortie
from django.utils.html import format_html


register = template.Library()


@register.simple_tag(takes_context=True)
def get_total_avoir_entree_by_product(context, entree):
    avoirs = AvoirSortie.objects.filter(entree=entree)
    if avoirs:
        avoirs = sum([a.qte_sortie for a in avoirs]) 
        return format_html("""
        {1}
        -
        <input type='hidden' name="entree" value="{2}" />
        <button type="submit" data-original-title="Tooltip on top" title="Total Avoir " class="btn btn-warning waves-effect">{0} </button>
              """.format(avoirs, entree.qte_entree ,entree.pk) )
    else:
        return str(entree.qte_entree)

@register.filter(name='msg_entree_deleted_avoir')
def msg_entree_deleted_avoir(value, arg):
    if value is None:
        return "cette entrée est supprimée"
    else:
        return value
    


