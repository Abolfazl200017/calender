from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    date = jmodels.jDateField()
    time = models.CharField(max_length=2)
    private = models.BooleanField(default=False)
    exepts = models.ManyToManyField(User, related_name='firends', blank=True)