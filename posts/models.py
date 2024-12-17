from django.db import models
class Category(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.title}"
class Tag(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.title}"
class Post(models.Model):
    category = models.ForeignKey(Category, models.CASCADE, null=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    title = models.CharField(max_length=100)   
    content = models.CharField(max_length=100)   
    rate = models.CharField(max_length=100, null=True,blank=True)   
    create_at = models.DateField(auto_now_add=True)   
    update_at = models.DateField(auto_now=True)   
    image = models.ImageField(null=True, blank=True) 
    def __str__(self):
        return f"title: {self.title}, category: {self.category}"