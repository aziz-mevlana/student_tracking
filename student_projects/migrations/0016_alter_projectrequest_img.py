# Generated by Django 5.1.3 on 2025-02-18 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_projects', '0015_alter_projectrequest_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectrequest',
            name='img',
            field=models.ImageField(default='default_project.jpg', null=True, upload_to='project_images/'),
        ),
    ]
