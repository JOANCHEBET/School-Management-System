# Generated by Django 4.2.7 on 2023-11-28 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joanApp', '0012_rename_name_teacher_name_remove_teacher_email_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Students',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='Name',
            new_name='Name1',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='description',
            new_name='description1',
        ),
        migrations.AddField(
            model_name='teacher',
            name='Name2',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='Name3',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='description2',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='description3',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
