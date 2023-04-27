from django.urls import path
from tasks.views import (
    create_task,
    show_my_tasks,
    add_note,
    task_detail,
    edit_task,
    delete_task,
)


urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", show_my_tasks, name="show_my_tasks"),
    path("note/", add_note, name="add_note"),
    path("<int:id>/", task_detail, name="task_detail"),
    path("task/<int:id>/", edit_task, name="edit_task"),
    path("delete/<int:id>/", delete_task, name="delete_task"),
]
