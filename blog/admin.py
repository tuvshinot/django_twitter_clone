from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_posted', 'author')
    list_display_links = ('id', 'title')
    list_filter = ('id', 'title')
    search_fields = ('id', 'type_order')
    list_per_page = 25

admin.site.register(Post, PostAdmin)