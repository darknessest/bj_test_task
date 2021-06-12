from django import forms


class TaskForm(forms.Form):
    user_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    task_text = forms.CharField(min_length=1)
