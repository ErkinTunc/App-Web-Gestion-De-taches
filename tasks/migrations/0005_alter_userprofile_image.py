# Generated by Django 5.2 on 2025-05-08 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='placeholder.png', max_length=500, upload_to='profile_pictures'),
        ),
    ]
