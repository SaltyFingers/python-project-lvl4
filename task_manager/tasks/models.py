from django.db import models
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.labels.models import Label
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Task(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        unique=True,
        verbose_name=_("Name")
    )

    description = models.TextField(
        null=False,
        verbose_name=_("Description")
    )

    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        related_name="tasks",
        verbose_name=_("Author")
    )

    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        null=True,
        related_name="tasks",
        verbose_name=_("Status")
    )

    labels = models.ManyToManyField(
        Label,
        related_name="tasks",
        blank=True,
        verbose_name=_("Labels")
    )

    executor = models.ForeignKey(
        User, on_delete=models.PROTECT,
        null=True,
        related_name="works_on",
        blank=True,
        verbose_name=_("Executor")
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
