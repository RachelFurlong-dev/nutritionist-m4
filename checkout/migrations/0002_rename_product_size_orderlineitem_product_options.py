# Generated by Django 3.2.19 on 2023-06-17 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='product_size',
            new_name='product_options',
        ),
    ]
