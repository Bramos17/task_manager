from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now_add=False)
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(
        "projects.Project",
        related_name="tasks",
        on_delete=models.CASCADE,
        null=True
    )
    assignee = models.ForeignKey(
        "auth.User",
        related_name="tasks",
        on_delete=models.CASCADE,
        null=True,
    )
