from django.contrib import admin
from .models import Things, Suplier, Order, Pos_order, Chegue

class ThingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'suplier', 'exist')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'price')
    list_editable = ('price', 'exist')
    list_filter = ('exist', 'suplier')

admin.site.register(Things, ThingsAdmin)

class SuplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'agent_name', 'agent_firstname', 'agent_patronymic', 'exist')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'agent_firstname')
    list_editable = ('exist',)
    list_filter = ('exist',)

admin.site.register(Suplier, SuplierAdmin)

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('date_create', 'date_finish', 'price', 'address_delivery', 'status',)
    list_display_links = ()
    search_fields = ()
    list_editable = ('date_finish', 'status')
    list_filter = ('status',)

admin.site.register(Order, OrderAdmin)

class Pos_orderAdmin(admin.ModelAdmin):
    list_display = ("thing", "order", "count", "price")
    list_display_links = ()
    search_fields = ()
    list_editable = ()
    list_filter = ()



admin.site.register(Pos_order, Pos_orderAdmin)

class ChegueAdmin(admin.ModelAdmin):
    list_display = ("date_print", "address_print", "terminal", "order")
    list_display_links = ()
    search_fields = ()
    list_editable = ()
    list_filter = ()



admin.site.register(Chegue, ChegueAdmin)

