from django.db import models


class Task(models.Model):
    """
        Model for a task
    """
    class Status(models.TextChoices):
        NOT_DONE = "не выполнено"
        ACTIVE = "в процессе"
        DONE = "выполнено"

    user_name = models.CharField(max_length=100)
    email = models.EmailField(null=False)
    task_text = models.TextField(null=False)
    edited_by_admin = models.BooleanField(default=False)

    task_status = models.CharField(
        max_length=100,
        choices=Status.choices,
        default=Status.NOT_DONE,
    )

    @property
    def was_edited_by_admin(self) -> bool:
        return self.edited_by_admin
