from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    img = models.ImageField(upload_to='blogpics')
    price = models.IntegerField()
    recommend = models.IntegerField()

class Comment(models.Model):
    blog_id = models.IntegerField()
    comment = models.CharField(max_length=200)
    review = models.IntegerField()