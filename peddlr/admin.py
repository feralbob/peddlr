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
    fields = ('slice_ref', 'mode', 'type_type', 'rng', 'aggregation_fn', 'operator', 'constant')
    readonly_fields = ('slice_ref', )
    list_display = ('slice_ref', 'mode', 'type_type', 'rng', 'aggregation_fn', 'operator', 'constant')


class ItemsAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ('name', 'timestamp', 'active', 'slice_ref', 'fraction', 'population', 'automated_email')
    readonly_fields = ('timestamp',)
    list_display = ('user', 'intervention', 'experimental', 'timestamp')


admin.site.register(Items, ItemsAdmin)
admin.site.register(Checkin, CheckinAdmin)
admin.site.register(CheckinItem, CheckinItemAdmin)
