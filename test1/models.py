from django.db import models

# Create your models here.

class Users(models.Model):
    chat_id = models.IntegerField(blank=True, null=True,default=None)
    def __str__(self):
        return str(self.chat_id)

class Messages(models.Model):
    chat = models.ForeignKey(Users,on_delete=models.CASCADE,default=None)
    message = models.CharField(blank=True, null=True,default="",max_length=255)
    date_created = models.DateTimeField(blank=True, null=True,auto_now=True)
    
    def __str__(self):
        return str(self.chat_id)