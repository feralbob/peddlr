from django.contrib import admin
from models import Checkin, Item


class CheckinAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ('seller_name', 'items', 'point', 'expiry_offset')
    list_display = ('seller_name', 'expiry')


class ItemsAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ('name',)
    list_display = ('name',)


admin.site.register(Item, ItemsAdmin)
admin.site.register(Checkin, CheckinAdmin)
