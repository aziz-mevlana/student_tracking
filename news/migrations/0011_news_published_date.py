# Generated by Django 5.1.3 on 2024-12-21 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_alter_news_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
