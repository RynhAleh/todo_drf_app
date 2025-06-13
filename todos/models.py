from django.db import models


# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Todo(models.Model):
    title = models.CharField(max_length=255)
    people = models.ForeignKey(People, on_delete=models.RESTRICT)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
