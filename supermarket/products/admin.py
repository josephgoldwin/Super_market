from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'price',
        'quantity',
        'extra_quantity',
        'total_amount',
        'created_at',
    )

    search_fields = ('product_name',)

    list_filter = ('created_at', 'updated_at')

    readonly_fields = ('total_amount', 'created_at', 'updated_at')

    ordering = ('-created_at',)
