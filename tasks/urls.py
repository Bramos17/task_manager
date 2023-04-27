from django.urls import path
from tasks.views import create_task, show_my_tasks, add_notes


urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", show_my_tasks, name="show_my_tasks"),
    path("note/", add_notes, name="add_notes"),
]
