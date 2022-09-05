from django.contrib import admin

from .models import Product

class ListingProducts(admin.ModelAdmin):
    list_display = ('id', 'name', 'price','description')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Product, ListingProducts)