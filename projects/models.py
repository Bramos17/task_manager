from django.db import models
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    tasks_completed = models.IntegerField()
    owner = models.ForeignKey(
        USER_MODEL,
        related_name="projects",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.name
