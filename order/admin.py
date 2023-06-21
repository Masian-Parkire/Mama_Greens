from django.contrib import admin

# Register your models here.
from .models import Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name','order_number','order_total','date')
admin.site.register(Order,OrderAdmin)
