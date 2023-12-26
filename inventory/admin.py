from django.contrib import admin

from django.contrib import admin
from .models import Category, Product, Supplier, invention
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("code", "desc",)

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("code", "desc", "count")

admin.site.register(Product, ProductAdmin)

class SupplierAdmin(admin.ModelAdmin):
    list_display = ("idettity", "firstname", "lastname", "phone", "city", "address")

admin.site.register(Supplier, SupplierAdmin)

class inventionAdmin(admin.ModelAdmin):
    list_display = ("product_code", "supplier_code", "count", "date")

admin.site.register(invention, inventionAdmin)

