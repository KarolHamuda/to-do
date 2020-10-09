from django.db import models
import uuid
from django.utils import timezone
from colorfield.fields import ColorField


class Task(models.Model):

    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    priority = ColorField(default='#FF0000')
    inserted_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "tasks"