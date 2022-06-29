from django.db import models
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.labels.models import Label

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=500, null=False)
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, related_name="tasks"
    )
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, null=True, related_name="tasks"
    )
    labels = models.ManyToManyField(Label,related_name="tasks", blank=True)
    executor = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, related_name="works_on"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
