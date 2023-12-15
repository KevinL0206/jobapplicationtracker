from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class jobApplication(models.Model):

    notApplied = 'Not Applied'
    applied = 'Applied'
    interview = 'Interview'

    statusOptions = [
        (notApplied, 'Not Applied'),
        (applied, 'Applied'),
        (interview,'Interview'),
    ]

    applicationID = models.AutoField(primary_key=True)
    companyName = models.CharField(default = None,max_length=255)
    jobDescription = models.TextField(default = None)
    jobLocation = models.CharField(default = None, max_length=255)
    applicationDate = models.DateField(default=None)
    jobDeadline = models.DateField(default = None)
    status = models.CharField(max_length=255,choices = statusOptions)
    
    
    userID = models.ForeignKey(User,on_delete=models.CASCADE)
    
