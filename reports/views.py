from django.shortcuts import render

from inventory.models import Item, Stock
from warehouses.models import Warehouse
from transactions.models import Receiving, Issue


def dashboard(request):

    total_stock = sum(
        Stock.objects.values_list(
            "quantity",
            flat=True
        )
    )


    low_stock_items = []

    for item in Item.objects.all():

        item_stock = sum(
            Stock.objects.filter(
                item=item
            ).values_list(
                "quantity",
                flat=True
            )
        )

        if item_stock <= item.minimum_stock:

            low_stock_items.append(
                {
                    "item": item,
                    "quantity": item_stock
                }
            )


    warehouse_data = []


    for warehouse in Warehouse.objects.all():

        quantity = sum(
            Stock.objects.filter(
                warehouse=warehouse
            ).values_list(
                "quantity",
                flat=True
            )
        )


        warehouse_data.append(
            {
                "name": warehouse.name,
                "quantity": quantity
            }
        )


    recent_receiving = Receiving.objects.all().order_by(
        "-id"
    )[:5]


    recent_issue = Issue.objects.all().order_by(
        "-id"
    )[:5]



    context = {

        "total_warehouses":
            Warehouse.objects.count(),


        "total_items":
            Item.objects.count(),


        "total_stock":
            total_stock,


        "total_receiving":
            Receiving.objects.count(),


        "total_issue":
            Issue.objects.count(),


        "low_stock_items":
            low_stock_items,


        "warehouse_data":
            warehouse_data,


        "recent_receiving":
            recent_receiving,


        "recent_issue":
            recent_issue,

    }


    return render(
        request,
        "reports/dashboard.html",
        context
    )

from inventory.models import Stock, Item



def report_home(request):

    return render(
        request,
        "reports/report_home.html"
    )



def stock_report(request):

    stocks = Stock.objects.all()


    context = {

        "stocks": stocks

    }


    return render(
        request,
        "reports/stock_report.html",
        context
    )




def low_stock_report(request):

    low_items = []


    for item in Item.objects.all():

        quantity = sum(
            Stock.objects.filter(
                item=item
            ).values_list(
                "quantity",
                flat=True
            )
        )


        if quantity <= item.minimum_stock:

            low_items.append(
                {
                    "item": item,
                    "quantity": quantity
                }
            )


    return render(
        request,
        "reports/low_stock.html",
        {
            "items": low_items
        }
    )