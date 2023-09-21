from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_login', 'username', 'email', 'phone', 'is_staff', 'mailing_list')
    list_display_links = ('id', 'last_login', 'username', 'email', 'phone',)
    search_fields = ('id', 'username', 'phone', 'email')
    list_filter = ('is_staff',)
    list_editable = ('is_staff', 'mailing_list')


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'price', 'stock', 'category', 'manufacturer')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('category', 'manufacturer', 'price',)
    list_editable = ('price', 'stock')
    prepopulated_fields = {'slug': ('name',)}


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'manufacturer_name', 'country', 'get_image')
    list_display_links = ('manufacturer_name',)
    search_fields = ('manufacturer_name', 'country')
    list_filter = ('country',)
    prepopulated_fields = {"slug": ("manufacturer_name",)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="60" height="60"')

    get_image.short_description = "Логотип"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    readonly_fields = ('image',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('name',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="60" height="60"')

    get_image.short_description = "Изображение категории"


class Discount_For_Product_CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'discount_percentage', 'discount_start_date', 'discount_end_date')
    list_display_links = ('id',)
    search_fields = ('category_name', 'discount_start_date', 'discount_end_date')
    list_filter = ('category_name', 'discount_start_date', 'discount_end_date')
    prepopulated_fields = {'slug': ('category_name', 'discount_start_date', 'discount_end_date')}
    list_editable = ('discount_end_date',)


class Product_ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_name', 'first_img', 'get_image')
    readonly_fields = ('get_image',)
    list_display_links = ('img_name',)
    prepopulated_fields = {'slug': ('img_name',)}
    search_fields = ('img_name',)
    list_editable = ('first_img',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.img.url} width="60" height="60"')

    get_image.short_description = "Изображение продукта"


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'text', 'rating', 'date')
    list_filter = ('rating', 'product')
    search_fields = ('user', 'product')


class EmailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('id', 'email')


class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('id', 'characteristic_name', 'value')
    list_display_links = ('id', 'characteristic_name')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Users, UserAdmin)
admin.site.register(Discount_For_Product_Category, Discount_For_Product_CategoryAdmin)
admin.site.register(Product_Images, Product_ImagesAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Emails, EmailsAdmin)
admin.site.register(Characteristic, CharacteristicAdmin)
