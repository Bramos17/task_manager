from django import forms
from tasks.models import Task, Note


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "start_date",
            "due_date",
            "project",
            "assignee",
            "notes",
        ]


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            "task",
            "notes",
        ]
