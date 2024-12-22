# Generated by Django 5.1.3 on 2024-12-22 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_projects', '0007_remove_studentsubmission_submission_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectrequest',
            name='projects_class',
            field=models.IntegerField(choices=[(1, 'Class 1'), (2, 'Class 2'), (3, 'Class 3'), (4, 'Class 4'), (5, 'Class 5')], null=True),
        ),
        migrations.AddField(
            model_name='studentsubmission',
            name='submission_class',
            field=models.IntegerField(choices=[(1, 'Class 1'), (2, 'Class 2'), (3, 'Class 3'), (4, 'Class 4'), (5, 'Class 5')], null=True),
        ),
        migrations.AddField(
            model_name='studentsubmission',
            name='submission_deadline',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='studentsubmission',
            name='submission_title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
