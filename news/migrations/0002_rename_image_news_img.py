# Generated by Django 5.1.3 on 2024-11-24 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='image',
            new_name='img',
        ),
    ]
