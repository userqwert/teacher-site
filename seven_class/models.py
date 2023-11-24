from django.db import models
from django.urls import reverse
import uuid


class Object7(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("object_detail", args=[str(self.id)])
