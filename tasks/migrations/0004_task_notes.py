# Generated by Django 4.2 on 2023-04-26 21:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0003_rename_assingee_task_assignee"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="notes",
            field=models.TextField(null=True),
        ),
    ]
