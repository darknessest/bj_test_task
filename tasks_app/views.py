from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Task
from .forms import TaskForm


def index(request):
    """
    Renderes main page with all tasks

    :param request:
    :return:
    """

    context = {'tasks': Task.objects.values(),
               'new_task_form': TaskForm()
               }

    return render(request, "htmls/tasks_app/index.html", context)


def add_new(request):
    """
    Adds new task to the database

    :param request:
    :return:
    """
    if request.method == 'POST':
        received_form = TaskForm(request.POST)
        if received_form.is_valid():
            new_task = Task(
                user_name=received_form.cleaned_data['user_name'],
                email=received_form.cleaned_data['email'],
                task_text=received_form.cleaned_data['task_text']
            )

            new_task.save()

        return HttpResponseRedirect('/index')


# todo: delete V
def AFK(request):
    return render(request, "htmls/AFK.html")


def sample_http_resp(request):
    return HttpResponse("hello from sample respose")
