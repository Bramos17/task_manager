# Generated by Django 4.2 on 2023-04-25 17:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0002_alter_task_start_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="assingee",
            new_name="assignee",
        ),
    ]