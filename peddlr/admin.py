from django.contrib import admin
from models import Checkin, CheckinItem, Items


#class Inline(admin.TabularInline):
#    model =


class CheckinAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ('seller_name', 'location', 'time', 'expiry')
    list_display = ('seller_name', 'location', 'time', 'expiry')


class CheckinItemAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ('price', 'unit', 'item', 'checkin', 'options')
    readonly_fields = ()
    list_display = ('price', 'unit', 'item', 'checkin', 'options')


class ItemsAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ('name',)
    list_display = ('name',)


admin.site.register(Items, ItemsAdmin)
admin.site.register(Checkin, CheckinAdmin)
admin.site.register(CheckinItem, CheckinItemAdmin)
