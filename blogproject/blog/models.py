from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 创建数据库模型  分类
class Category(models.Model):
	name = models.CharField(max_length=150)
	def __str__(self):
		return self.name
		
#  标签
class Tag(models.Model):
	name = models.CharField(max_length=150)
	def __str__(self):
		return self.name
		
#  文章
class Post(models.Model):
	
	title = models.CharField(max_length=200)
	body = models.TextField()
	
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	
	category = models.ForeignKey( Category )
	tag = models.ManyToManyField( Tag, blank=True )
	
	author = models.ForeignKey( User )
	
	def __str__(self):
		return self.title