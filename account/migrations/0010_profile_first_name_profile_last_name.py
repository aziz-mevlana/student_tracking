# Generated by Django 5.1.3 on 2024-12-08 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_profile_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=16, null=True),
        ),
    ]