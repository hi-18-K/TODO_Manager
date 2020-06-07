from django.db import models                    #creating models
import datetime                                 #for adding datetime functionality
from threading import local
import pytz
from django.contrib.auth.models import User     #for adding login functionality



class Todo(models.Model):              #Our todolist model
    text = models.CharField(max_length=200)
    priority = models.CharField(max_length=8, default="", editable=True)
    type = models.CharField(max_length=20,default="", editable=True)
    duedate = models.DateTimeField(default=datetime.datetime.now(), blank=True,editable=True)
    #duetime = models.DateTimeField(default=datetime.datetime.now(), blank=True,editable=True)
    #author = models.CharField(max_length=10, default=User, editable=False)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text
