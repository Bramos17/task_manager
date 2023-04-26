from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm
from tasks.models import Task


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.save()
        return redirect("home")
    else:
        form = TaskForm()
    context = {"form": form}
    return render(request, "tasks/create_task.html", context)


@login_required
def show_my_tasks(request):
    show_my_tasks = Task.objects.filter(assignee=request.user)
    context = {"show_my_tasks": show_my_tasks}
    return render(request, "tasks/show_my_tasks.html", context)
