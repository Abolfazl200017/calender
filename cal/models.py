from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField()
    time = models.CharField(max_length=2)
    private = models.BooleanField(default=False)
    exepts = models.CharField(1)