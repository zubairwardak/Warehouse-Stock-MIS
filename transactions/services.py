from inventory.models import Stock



def increase_stock(
        item,
        warehouse,
        location,
        quantity
):

    stock, created = Stock.objects.get_or_create(
        item=item,
        warehouse=warehouse,
        location=location,
        defaults={
            "quantity": 0
        }
    )

    stock.quantity += quantity
    stock.save()

    return stock



def decrease_stock(
        item,
        warehouse,
        location,
        quantity
):

    stock, created = Stock.objects.get_or_create(
        item=item,
        warehouse=warehouse,
        location=location,
        defaults={
            "quantity": 0
        }
    )


    if stock.quantity < quantity:

        raise Exception(
            f"Insufficient stock. Available: {stock.quantity}"
        )


    stock.quantity -= quantity
    stock.save()


    return stock