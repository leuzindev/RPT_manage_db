from django.contrib import admin

from .models import User

class ListingUsers(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(User, ListingUsers)