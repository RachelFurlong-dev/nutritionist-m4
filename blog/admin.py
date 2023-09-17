from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'body', 'publish_date', 'thumb', 'author', 'status',)


admin.site.register(Post, PostAdmin)