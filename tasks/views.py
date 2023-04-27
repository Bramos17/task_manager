from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm, AddNoteForm
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


@login_required
def add_note(request):
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            note.save()
        return redirect("show_my_tasks")
    else:
        form = AddNoteForm()
    context = {"form": form}
    return render(request, "tasks/add_note.html", context)


@login_required
def task_detail(request, id):
    task = Task.objects.get(id=id)
    context = {"task": task}
    return render(request, "tasks/task_detail.html", context)


@login_required
def edit_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_detail", id=id)
    else:
        form = TaskForm(instance=task)
    context = {"form": form}
    return render(request, "tasks/edit_task.html", context)


@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        task.delete()
        return redirect("show_my_tasks")
    context = {"task": task}
    return render(request, "tasks/delete_task.html", context)

