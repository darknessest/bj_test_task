from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from tasks_app.models import Task
from tasks_app.forms import TaskForm


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
    if request.method == 'GET':
        tmp_task = Task.objects.get(pk=task_id)
        context = {
            'task_text': tmp_task.task_text,
            'task_status': tmp_task.task_status,
        }

        return JsonResponse(context)

    elif request.method == 'POST':
        print(request.POST)

        task_to_edit = Task.objects.get(pk=task_id)
        task_to_edit.task_text = request.POST['task text']
        task_to_edit.edited_by_admin = request.user.is_superuser
        task_to_edit.save()

        # todo: add save success
        return HttpResponseRedirect('/')


# def get_task_form_by_id(request, task_id):
#     if request.method == 'GET':
#         task_text = Task.objects.get(pk=task_id).task_text
#         # task_form = TaskForm.
#         context = {
#             'task_form': task_form
#         }
#
#         return render(request, "htmls/tasks_app/edit_task.html", context)
#
#     elif request.method == 'POST':
#         print(request.POST)
#
#         task_to_edit = Task.objects.get(pk=task_id)
#         task_to_edit.task_text = request.POST['task text']
#         task_to_edit.edited_by_admin = request.user.is_superuser
#         task_to_edit.save()
#
#         # todo: add save success
#         return HttpResponseRedirect('/')


# todo: delete V
def AFK(request):
    import urbandictionary as ud

    stuff = ud.random()
    # print(stuff)
    return render(request, "htmls/AFK.html", {'ud_word': stuff})


def test(request):
    return render(request, "htmls/test.html", )


def sample_http_resp(request):
    return HttpResponse("hello from sample respose")
