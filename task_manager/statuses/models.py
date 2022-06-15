from django.db import models

# Create your models here.


class Status(models.Model):
    name = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
