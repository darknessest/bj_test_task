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
        # todo: add success response
        return HttpResponseRedirect('/')


def edit_task(request, task_id):
    # print(request)
    if request.method == 'GET':
        task_text = Task.objects.get(pk=task_id).task_text
        context = {
            'task_text': task_text,
            'task_id': task_id,
        }

        return render(request, "htmls/tasks_app/edit_task.html", context)

    elif request.method == 'POST':
        print(request.POST)

        task_to_edit = Task.objects.get(pk=task_id)
        task_to_edit.task_text = request.POST['task text']
        task_to_edit.edited_by_admin = request.user.is_superuser
        task_to_edit.save()

        # todo: add save success
        return HttpResponseRedirect('/')


# todo: delete V
def AFK(request):
    return render(request, "htmls/AFK.html")


def sample_http_resp(request):
    return HttpResponse("hello from sample respose")
