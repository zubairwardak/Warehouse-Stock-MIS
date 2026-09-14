from django.shortcuts import render

from .models import Item, Stock



def item_list(request):

    items = Item.objects.all()


    context = {

        "items": items

    }


    return render(
        request,
        "inventory/item_list.html",
        context
    )