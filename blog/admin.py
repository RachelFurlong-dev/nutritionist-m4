from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'slug', 'publish_date', 'status',)
    list_filter = ("status",)
    search_fields = ['post_title', 'body']
    prepopulated_fields = {'slug': ('post_title',)}


admin.site.register(Post, PostAdmin)