from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS_CHOICE = (
    ("completed", "Completed"),
    ("not_completed", "Not Completed"),
)

'''
class User(models.Model):
    name = models.CharField(max_length=25)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=70, unique=True)
'''
class BillTask(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=16, choices=STATUS_CHOICE, default="not_completed")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class BillTag(models.Model):
    name = models.CharField(max_length=30)
    task = models.ManyToManyField(BillTask)

