# Generated by Django 3.2.19 on 2023-09-17 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-publish_date']},
        ),
    ]
