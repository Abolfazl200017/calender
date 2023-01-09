from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    date = models.DateTimeField()
    time = models.CharField(max_length=2)
    private = models.BooleanField(default=False)
    exepts = models.ManyToManyField(User, related_name='firends', blank=True)