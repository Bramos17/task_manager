from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.save()
        return redirect("home")
    else:
        form = TaskForm()
    context = {"form": form}
    return render(request, "tasks/create_task.html", context)
