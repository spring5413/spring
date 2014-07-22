# -*- coding:UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This field is required.
    user = models.ForeignKey(User,unique=True)
    location = models.CharField(max_length=140) 

