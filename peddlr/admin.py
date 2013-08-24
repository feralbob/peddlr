from django.contrib import admin
from models import Checkin, CheckinItem, Item


class CheckinItemInline(admin.TabularInline):
    model = CheckinItem
    fields = ('item', 'price', 'unit', 'checkin',)
    extra = 1


class CheckinAdmin(admin.ModelAdmin):
    save_on_top = True
    inlines = (CheckinItemInline, )
    fields = ('seller_name', 'location', 'expiry')
    list_display = ('seller_name', 'location', 'time', 'expiry')


class CheckinItemAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ('price', 'unit', 'item', 'checkin',)
    readonly_fields = ()
    list_display = ('price', 'unit', 'item', 'checkin',)


class ItemsAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ('name',)
    list_display = ('name',)


admin.site.register(Item, ItemsAdmin)
admin.site.register(Checkin, CheckinAdmin)
admin.site.register(CheckinItem, CheckinItemAdmin)
