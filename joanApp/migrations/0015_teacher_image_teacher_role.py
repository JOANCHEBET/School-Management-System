# Generated by Django 4.2.7 on 2023-11-28 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joanApp', '0014_rename_description1_teacher_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='role',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
