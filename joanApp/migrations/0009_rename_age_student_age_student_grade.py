# Generated by Django 4.2.7 on 2023-11-21 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joanApp', '0008_rename_h3_student_age_remove_student_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Age',
            new_name='age',
        ),
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
