# Generated by Django 4.2.7 on 2023-11-28 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joanApp', '0013_rename_student_students_rename_name_teacher_name1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='description1',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='Name1',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='Name2',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='Name3',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='description2',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='description3',
        ),
    ]