from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'status',
        'business',
        'created_by',
        'created_at',
    )
    list_filter = ('status', 'business')
    search_fields = ('name', 'description')
