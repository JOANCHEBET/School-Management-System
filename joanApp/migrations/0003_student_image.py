# Generated by Django 4.2.7 on 2023-11-18 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joanApp', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]