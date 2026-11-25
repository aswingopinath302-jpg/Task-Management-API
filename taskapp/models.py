from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    status = models.CharField(max_length=50, default="pending")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title