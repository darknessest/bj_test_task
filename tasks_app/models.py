from django.db import models

Status = ((0, 'not done'),
          (1, 'not done edited'),
          (10, 'done'),
          (11, 'done edited'))


class Task(models.Model):
    """
        Model for a task
    """
    # todo: edit V

    user_name = models.CharField(max_length=100)
    email = models.EmailField(null=False)
    task_text = models.TextField(null=False)
    edited_by_admin = models.BooleanField(default=False)

    task_status = models.IntegerField(
        choices=Status,
        default=0
    )
