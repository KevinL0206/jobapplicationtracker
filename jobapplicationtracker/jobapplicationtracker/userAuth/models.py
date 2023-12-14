from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class company(models.Model):
    companyID = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=255)
    jobDescription = models.TextField()
    jobLocation = models.CharField(max_length=255)
    jobDeadline = models.DateField()

class jobApplication(models.Model):
    applicationID = models.AutoField(primary_key=True)
    status = models.CharField(max_length=255)
    applicationDate = models.DateField(default=None)
    userID = models.ForeignKey(User,on_delete=models.CASCADE)
    companyID = models.ForeignKey(company,on_delete=models.CASCADE)
