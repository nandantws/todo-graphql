from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):

    status_choices = (
        ('1', 'Pending'),
        ('2', 'In Progress'),
        ('3', 'Completed'),
    )
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    status = models.CharField(
        max_length=20, choices=status_choices, default='1')
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title