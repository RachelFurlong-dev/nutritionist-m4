from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    # Specify the fields to be displayed in the admin list view
    list_display = ('post_title', 'slug', 'publish_date', 'status',)

    # Add a filter sidebar for the 'status' field
    list_filter = ("status",)

    # Enable search functionality for the specified fields
    search_fields = ['post_title', 'body']

    # Automatically populate the 'slug' field based on the 'post_title'
    prepopulated_fields = {'slug': ('post_title',)}


# Register the Post model with the custom admin configuration
admin.site.register(Post, PostAdmin)