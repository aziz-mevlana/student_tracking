# Generated by Django 5.1.3 on 2025-02-18 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_projects', '0013_alter_studentsubmission_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectrequest',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='project_images/'),
        ),
    ]
