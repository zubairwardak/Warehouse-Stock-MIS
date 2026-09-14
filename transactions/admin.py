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


admin.site.register(Receiving)
admin.site.register(ReceivingItem)

admin.site.register(Issue)
admin.site.register(IssueItem)

admin.site.register(Transfer)
admin.site.register(TransferItem)

admin.site.register(Return)