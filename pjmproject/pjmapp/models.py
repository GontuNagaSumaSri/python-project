from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class UserSignup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15,null=True)
    image = models.FileField(null=True)
    address = models.CharField(max_length=300,null=True,default=None)
    regdate = models.DateTimeField(auto_now_add=True,blank=True)
    def _str_(self):
      return self.user.username

class Job(models.Model):
    jobname=models.CharField(max_length=100,null=True)
    image = models.FileField(null=True)
    IndustryPractices=models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=300,null=True)
    startdate=models.DateField(null=True)
    enddate=models.DateField(null=True)
    venue=models.CharField(max_length=300,null=True)
    entryprice=models.CharField(max_length=100,null=True)
    creationdate = models.DateTimeField(default=datetime.now, blank=True)
    def _str_(self):
      return self.jobname

class SponsorTbl(models.Model):
    job =models.ForeignKey(Job,on_delete=models.CASCADE)
    sponsorimage = models.FileField(null=True)
    creationdate = models.DateTimeField(default=datetime.now, blank=True)
    def _str_(self):
      return self.job.jobname

class IndustryPractices(models.Model):
    industrypractices=models.CharField(max_length=100,null=True)
    creationdate = models.DateTimeField(default=datetime.now, blank=True)
    def _str_(self):
      return self.industrypractices

class Booking(models.Model):
    userinfo =models.ForeignKey(UserSignup,on_delete=models.CASCADE)
    eventinfo = models.ForeignKey(Job, on_delete=models.CASCADE)
    person=models.CharField(max_length=100,null=True)
    total=models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=20,null=True)
    bookingdate = models.DateField(null=True)
    cardno = models.CharField(max_length=20,null=True)
    cvv = models.CharField(max_length=10,null=True)
    expirydate = models.CharField(max_length=50,null=True)
    def _str_(self):
      return self.id