from django.contrib import admin
from .models import Product,Category,Cart

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title']


#admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','quantity','price','discount','status','created_at','updated_at','category']
    prepopulated_fields={'slug':('name',)}
    list_editable=['quantity','price','discount','status']
    list_filter=['status','created_at','updated_at']

@admin.register(Cart)
class CartAadmin(admin.ModelAdmin):
    pass

