# Generated by Django 3.0.7 on 2020-06-11 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='D:\\infa\\spadaroznik_git\\spadaroznik/templates/default.png', upload_to='profiles/'),
        ),
    ]