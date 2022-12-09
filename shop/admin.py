from django.contrib import admin
from .models import SaleProduct, FeaturedProduct, CollectionProduct, HeroProduct, PromoProduct


@admin.register(SaleProduct)
class SaleProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'detail',
                    'image', 'available']
    list_editable = ['image', 'available']
    prepopulated_fields = {'slug': ('name',)}  


@admin.register(FeaturedProduct)
class FeaturedProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_name', 'text',
                    'price', 'image', 'available']
    list_editable = ['price', 'image', 'available']



@admin.register(CollectionProduct)
class CollectionProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image', 'available']
    list_editable = ['image', 'available']
    prepopulated_fields = {'slug': ('name',)}  


@admin.register(HeroProduct)
class HeroProduct(admin.ModelAdmin):
    list_display = ['name', 'slug', 'text',
                    'available', 'image']
    list_editable = ['available', 'image']
    prepopulated_fields = {'slug': ('name',)}  



@admin.register(PromoProduct)
class PromoProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date',
                    'image', 'available']
    list_editable = ['image', 'available']
