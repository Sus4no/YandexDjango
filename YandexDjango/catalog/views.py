from django.shortcuts import render


def item_list(request):
    template_name = 'catalog/index.html'
    context = {}
    return render(request, template_name, context)


def item_detail(request, pk):
    template_name = 'catalog/item.html'
    context = {'num': pk}
    return render(request, template_name, context)
