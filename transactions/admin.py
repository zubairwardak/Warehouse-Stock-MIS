from django.contrib import admin

from .models import (
    Receiving,
    ReceivingItem,
    Issue,
    IssueItem,
    Transfer,
    TransferItem,
    Return
)


@admin.register(Receiving)
class ReceivingAdmin(admin.ModelAdmin):

    list_display = (
        "voucher_no",
        "warehouse",
        "supplier",
        "received_by",
        "date"
    )

    list_filter = (
        "warehouse",
        "date"
    )



admin.site.register(ReceivingItem)



@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):

    list_display = (
        "voucher_no",
        "department",
        "warehouse",
        "status",
        "approved_by",
        "date"
    )


    list_filter = (
        "status",
        "warehouse",
        "date"
    )


    search_fields = (
        "voucher_no",
        "department"
    )



admin.site.register(IssueItem)



@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):

    list_display = (
        "voucher_no",
        "from_warehouse",
        "to_warehouse",
        "approved_by",
        "date"
    )


admin.site.register(TransferItem)



@admin.register(Return)
class ReturnAdmin(admin.ModelAdmin):

    list_display = (
        "voucher_no",
        "item",
        "quantity",
        "condition",
        "date"
    )