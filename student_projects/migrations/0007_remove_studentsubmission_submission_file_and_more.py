# Generated by Django 5.1.3 on 2024-12-22 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_projects', '0006_projectrequest_studentsubmission_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentsubmission',
            name='submission_file',
        ),
        migrations.AddField(
            model_name='studentsubmission',
            name='submission_description',
            field=models.TextField(null=True),
        ),
    ]