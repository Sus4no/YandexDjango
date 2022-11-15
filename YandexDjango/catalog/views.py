from django.shortcuts import render
from catalog.models import Item


def item_list(request):
    template_name = 'catalog/index.html'
    items = Item.objects.on_item_list()
    context = {
        'items': items,
    }
    return render(request, template_name, context)


def item_detail(request, pk):
    template_name = 'catalog/item.html'
    item = Item.objects.on_item_detail(pk=pk)
    context = {'item': item[0]}
    return render(request, template_name, context)
