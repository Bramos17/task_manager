from django import forms
from tasks.models import Task, Note


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "start_date",
            "due_date",
            "is_completed",
            "project",
            "assignee",
            "notes",
        ]
        widgets = {
            "is_completed":
                forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            "task",
            "notes",
        ]
