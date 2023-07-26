from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)
    # models.cascade is for if user gets deleted all data should be deleted of that user
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    # category = models.CharField(max_length=50)

    # default value of model
    def __str__(self):
        return self.title
    
    # default ordering whose status is completed all those will be at bottom
    class Meta:
        ordering = ['status']

