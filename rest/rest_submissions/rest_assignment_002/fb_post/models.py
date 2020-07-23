from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    name=models.CharField(max_length=100)
    profile_pic=models.URLField()

class Post(models.Model):
    content=models.CharField(max_length=1000)
    posted_at=models.DateTimeField(auto_now=True)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')

class Comment(models.Model):
    content=models.CharField(max_length=1000)
    commented_at=models.DateTimeField(auto_now=True)
    commented_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    parent_comment=models.ForeignKey('self',on_delete=models.CASCADE,null=True,related_name='replies')


    
class Reaction(models.Model):
    reactions=(('WOW','WOW'),
    ('LIT','LIT'),
    ('LOVE','LOVE'),
    ('HAHA','HAHA'),
    ('THUMBS-UP','THUMBS-UP'),
    ('THUMBS-DOWN','THUMBS-DOWN'),
    ('ANGRY','ANGRY'),
    ('SAD','SAD'))
    post=models.ForeignKey(Post,on_delete=models.CASCADE,null=True,related_name='reactions')
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE,null=True,related_name='reactions')
    reaction=models.CharField(max_length=100,choices=reactions)
    reacted_at=models.DateTimeField(auto_now=True)
    reacted_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='reactions')

