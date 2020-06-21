# Generated by Django 3.0.7 on 2020-06-21 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Участник', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата сообщения')),
                ('is_readed', models.BooleanField(default=False, verbose_name='Прочитано')),
                ('Пользователь', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('Чат', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chats.Chat')),
            ],
            options={
                'ordering': ['pub_date'],
            },
        ),
    ]
