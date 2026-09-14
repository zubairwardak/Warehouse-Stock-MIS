from django.contrib import admin

from .models import Category, Unit, Item, Stock


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
    )



@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'symbol'
    )



@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    list_display = (
        'code',
        'name',
        'category',
        'unit'
    )



@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):

    list_display = (
        'item',
        'warehouse',
        'location',
        'quantity'
    )