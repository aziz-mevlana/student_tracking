# Generated by Django 5.1.3 on 2025-02-20 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_projects', '0021_alter_projectrequest_submision_start'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectrequest',
            old_name='submision_start',
            new_name='submission_start',
        ),
    ]
