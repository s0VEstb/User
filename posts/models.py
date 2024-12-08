from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)   
    content = models.CharField(max_length=100)   
    rate = models.CharField(max_length=100, null=True,blank=True)   
    create_at = models.DateField(auto_now_add=True)   
    update_at = models.DateField(auto_now=True)   
    def __str__(self):
        return f"{self.title}, content :{self.content}"