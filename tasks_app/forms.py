from django import forms

from tasks_app.models import Status


class TaskForm(forms.Form):
    user_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    task_text = forms.CharField(widget=forms.Textarea, min_length=1)
    task_status = forms.ChoiceField(choices=Status)
