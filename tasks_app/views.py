from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from tasks_app.models import Task
from tasks_app.forms import TaskForm

response_base_ok = {"status": "ok", "message": {}}
response_create_bad = {"status": "error", "message": {
    "username": "Поле является обязательным для заполнения",
    "email": "Неверный email",
    "text": "Поле является обязательным для заполнения"
}}


def index(request):
    """
    Renderes main page with all tasks

    :param request:
    :return:
    """

    context = {'tasks': Task.objects.all(),
               'new_task_form': TaskForm(),
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
    if request.method == 'GET':
        tmp_task = Task.objects.get(pk=task_id)
        context = {
            'task_text': tmp_task.task_text,
            'task_status': tmp_task.task_status,
        }

        return JsonResponse(context)

    elif request.method == 'POST':
        task_to_edit = Task.objects.get(pk=task_id)
        task_to_edit.task_text = request.POST['task text']

        task_to_edit.task_status = request.POST['task status']
        task_to_edit.edited_by_admin = request.user.is_superuser
        task_to_edit.save()

        # todo: add save success
        return HttpResponseRedirect('/')
