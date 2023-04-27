from django.shortcuts import render, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm


@login_required
def list_projects(request):
    list_project = Project.objects.filter(owner=request.user)
    context = {"list_projects": list_project}
    return render(request, "projects/list_projects.html", context)


@login_required
def show_project(request, id):
    Show_project = Project.objects.get(id=id)
    context = {"show_project": Show_project}
    return render(request, "projects/show_project.html", context)


@login_required
def Create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
    context = {"form": form}
    return render(request, "projects/create_project.html", context)


@login_required
def search_projects(request):
    query = request.GET.get('q')
    if query:
        list_projects = Project.objects.filter(name__icontains=query).values(
            "name",
            "description",
            "owner__username",
        )
    else:
        list_projects = Project.objects.none()
    context = {"list_projects": list_projects}
    return render(request, 'projects/search_results.html', context)
