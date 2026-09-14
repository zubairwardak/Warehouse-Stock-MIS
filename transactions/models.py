from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User
from warehouses.models import Warehouse
from inventory.models import Item
from .services import increase_stock, decrease_stock



# ==============================
# Receiving Materials
# ==============================

class Receiving(models.Model):

    voucher_no = models.CharField(
        max_length=50,
        unique=True
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.PROTECT
    )

    received_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )

    supplier = models.CharField(
        max_length=150
    )

    date = models.DateField(
        auto_now_add=True
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )


    def __str__(self):
        return self.voucher_no



class ReceivingItem(models.Model):

    receiving = models.ForeignKey(
        Receiving,
        related_name="items",
        on_delete=models.CASCADE
    )

    item = models.ForeignKey(
        Item,
        on_delete=models.PROTECT
    )

    quantity = models.PositiveIntegerField()


    def __str__(self):
        return self.item.name



# ==============================
# Issue Materials
# ==============================

class Issue(models.Model):

    voucher_no = models.CharField(
        max_length=50,
        unique=True
    )


    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )


    department = models.CharField(
        max_length=150
    )


    receiver = models.ForeignKey(
        User,
        related_name="received_materials",
        on_delete=models.PROTECT
    )


    issued_by = models.ForeignKey(
        User,
        related_name="issued_materials",
        on_delete=models.PROTECT
    )


    date = models.DateField(
        auto_now_add=True
    )


    purpose = models.TextField()



    def __str__(self):
        return self.voucher_no




class IssueItem(models.Model):

    issue = models.ForeignKey(
        Issue,
        related_name="items",
        on_delete=models.CASCADE
    )


    item = models.ForeignKey(
        Item,
        on_delete=models.PROTECT
    )


    quantity = models.PositiveIntegerField()



# ==============================
# Warehouse Transfer
# ==============================


class Transfer(models.Model):

    voucher_no = models.CharField(
        max_length=50,
        unique=True
    )


    from_warehouse = models.ForeignKey(
        Warehouse,
        related_name="transfer_out",
        on_delete=models.PROTECT
    )


    to_warehouse = models.ForeignKey(
        Warehouse,
        related_name="transfer_in",
        on_delete=models.PROTECT
    )


    approved_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )


    date = models.DateField(
        auto_now_add=True
    )


    def __str__(self):
        return self.voucher_no





class TransferItem(models.Model):

    transfer = models.ForeignKey(
        Transfer,
        related_name="items",
        on_delete=models.CASCADE
    )


    item = models.ForeignKey(
        Item,
        on_delete=models.PROTECT
    )


    quantity = models.PositiveIntegerField()




# ==============================
# Returned Materials
# ==============================


class Return(models.Model):

    voucher_no = models.CharField(
        max_length=50,
        unique=True
    )


    item = models.ForeignKey(
        Item,
        on_delete=models.PROTECT
    )


    quantity = models.PositiveIntegerField()


    returned_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )


    condition = models.CharField(
        max_length=50
    )


    date = models.DateField(
        auto_now_add=True
    )


    def __str__(self):
        return self.voucher_no




# ==============================
# Automatic Stock Update
# ==============================


@receiver(
    post_save,
    sender=ReceivingItem
)
def update_stock_after_receiving(
        sender,
        instance,
        created,
        **kwargs
):

    if created:

        increase_stock(
            item=instance.item,
            warehouse=instance.receiving.warehouse,
            location=instance.receiving.warehouse.locations.first(),
            quantity=instance.quantity
        )




@receiver(
    post_save,
    sender=IssueItem
)
def update_stock_after_issue(
        sender,
        instance,
        created,
        **kwargs
):

    if created:

        decrease_stock(
            item=instance.item,
            warehouse=instance.issue.warehouse,
            location=instance.issue.warehouse.locations.first(),
            quantity=instance.quantity
        )