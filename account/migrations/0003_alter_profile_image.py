# Generated by Django 5.1.3 on 2024-12-03 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/uploads/profile_pics/default.jpg', upload_to='profile_pics'),
        ),
    ]
