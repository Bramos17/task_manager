from django.urls import path
from projects.views import (
            list_projects,
            show_project,
            Create_project,
)


urlpatterns = [
    path("", list_projects, name="list_projects"),
    path("<int:id>/", show_project, name="show_project"),
    path("create/", Create_project, name="create_project"),
]
