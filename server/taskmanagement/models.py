from django.conf import settings
from django.db import models
from .enum import Status, Proirity

class Task(models.Model):
    task_name = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateTimeField()
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null = True,
    )
    status = models.PositiveSmallIntegerField(
        default=1,
        choices=[(e.value, e.name) for e in Status]
    )
    started_at = models.DateTimeField(null=True)
    closed_at = models.DateTimeField(null=True)
    priority = models.PositiveSmallIntegerField(
        default=1,
        choices=[(e.value, e.name) for e in Proirity]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    