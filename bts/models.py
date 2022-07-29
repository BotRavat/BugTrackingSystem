from django.db import models
from sqlite3 import Timestamp

# Create your models here.


class AddBug(models.Model):
    sno=models.AutoField(primary_key=True)
    bugname=models.CharField(max_length =255)
    bugdate=models.CharField(max_length=13)
    bugpriority=models.CharField(max_length=100)
    projectname=models.CharField(max_length=100,default='testproject')
    content=models.TextField()
   # username=models.CharField(max_length=100)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
       return 'Bug Name - '+self.bugname 



class AddProject(models.Model):
    sno=models.AutoField(primary_key=True)
    projectname=models.CharField(max_length=255)
    projectmanager=models.CharField(max_length=255)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)

       