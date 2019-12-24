
from django.contrib import admin
from .models import Product,Category,Brand

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand' , 'category','specification')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category',)


# @admin.register(Specification)
# class SpecificationAdmin(admin.ModelAdmin):
#     list_display = ('key', 'value', 'unit')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)