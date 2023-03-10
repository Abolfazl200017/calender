# Generated by Django 4.1.5 on 2023-01-10 11:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0002_remove_todo_exepts_alter_todo_title_todo_exepts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='exepts',
            field=models.ManyToManyField(blank=True, related_name='firends', to=settings.AUTH_USER_MODEL),
        ),
    ]
