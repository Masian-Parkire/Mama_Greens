from django.contrib import admin

# Register your models here.
from .models import Vendor
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name','contact','store_name','password','username')
admin.site.register(Vendor,VendorAdmin)
