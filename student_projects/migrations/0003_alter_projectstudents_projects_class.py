# Generated by Django 5.1.3 on 2024-12-22 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_projects', '0002_projectstudents_projects_class_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectstudents',
            name='projects_class',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
