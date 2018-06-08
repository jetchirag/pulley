# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Jobs(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=10)
    
    # Email to which user will be notified 
    # Notify or not, when to notify/level are defined in schedule model
    email = models.CharField(max_length=50)
    
    # Below are defined login details which are mostly common to all types
    hostname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    port = models.SmallIntegerField()
    
    # Below are defined parameters which are applicable to some types
    remotepath = models.CharField(max_length=100, null=True, blank=True)
    ssl = models.IntegerField(default=0, null=True, blank=True) # Enable/Disable
    
    # Some information about job
    lastrun = models.DateTimeField(blank=True, null=True)
    state = models.IntegerField(default=1) # Enable/Disable