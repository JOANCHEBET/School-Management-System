# Generated by Django 4.2.7 on 2023-11-27 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joanApp', '0010_remove_student_grade_student_image_alter_student_age_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='teachers',
            new_name='Teacher',
        ),
    ]
