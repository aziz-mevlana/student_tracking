# Generated by Django 5.1.3 on 2025-04-12 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_projects', '0024_alter_weeksubmission_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeksubmission',
            name='is_approved',
            field=models.IntegerField(choices=[(0, 'Waiting for Approval'), (1, 'Approved'), (2, 'Not Approved')], default=0),
        ),
    ]
