# Generated by Django 4.1.5 on 2023-01-24 15:06

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todo_body_alter_todo_exepts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=django_jalali.db.models.jDateField(),
        ),
    ]
