from django.apps import AppConfig


class BlogConfig(AppConfig):
    # Define the default auto field for model migrations
    default_auto_field = 'django.db.models.BigAutoField'

    # Set the name of the app
    name = 'blog'

