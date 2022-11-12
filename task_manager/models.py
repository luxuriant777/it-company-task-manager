from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Worker(AbstractUser):
    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"
        ordering = ['first_name']

    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Task(models.Model):
    class Meta:
        ordering = ["priority"]

    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField()
    PRIORITY_CHOICES = [
        (1, "Urgent"),
        (2, "High"),
        (3, "Medium"),
        (4, "Low"),
    ]
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default="low")
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker, related_name="tasks")

    def __str__(self) -> str:
        return f"{self.name} (Priority: {self.priority})"
