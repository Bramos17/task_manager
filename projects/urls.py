from django.urls import path
from projects.views import (
    list_projects,
    show_project,
    Create_project,
    search_projects,
    edit_project,
    delete_project,
)


urlpatterns = [
    path("", list_projects, name="list_projects"),
    path("<int:id>/", show_project, name="show_project"),
    path("create/", Create_project, name="create_project"),
    path("search", search_projects, name="search_projects"),
    path("projects/<int:id>/", edit_project, name="edit_project"),
    path("delete/<int:id>/", delete_project, name="delete_project"),
]
