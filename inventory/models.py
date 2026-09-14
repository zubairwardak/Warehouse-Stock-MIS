from django.db import models
from warehouses.models import Warehouse, StorageLocation


class Category(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )


    def __str__(self):
        return self.name



class Unit(models.Model):

    name = models.CharField(
        max_length=50,
        unique=True
    )

    symbol = models.CharField(
        max_length=20
    )


    def __str__(self):
        return self.name



class Item(models.Model):

    code = models.CharField(
        max_length=50,
        unique=True
    )

    name = models.CharField(
        max_length=150
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
    )

    unit = models.ForeignKey(
        Unit,
        on_delete=models.PROTECT
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    serial_required = models.BooleanField(
        default=False
    )

    minimum_stock = models.PositiveIntegerField(
        default=0
    )


    def __str__(self):
        return f"{self.code} - {self.name}"



class Stock(models.Model):

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE
    )

    location = models.ForeignKey(
        StorageLocation,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        default=0
    )

    last_updated = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return f"{self.item.name} - {self.quantity}"