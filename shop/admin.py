from django.contrib import admin
from .models import *


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'price', 'stock', 'category', 'manufacturer')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('category', 'manufacturer', 'price',)
    list_editable = ('price', 'stock')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(Users)
admin.site.register(Discount_For_Product_Category)
admin.site.register(Product_Images)
admin.site.register(Comments)
admin.site.register(Emails)
admin.site.register(Characteristic)
