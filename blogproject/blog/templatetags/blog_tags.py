from ..models import Post, Category
from django import template

#  实例化一个 template.Library 类
register = template.Library()

#  使用装饰器注册函数为模板标签
#  之后就可以在模板中使用此标签
@register.simple_tag
def get_recent_posts(num=5):
	return Post.objects.all().order_by("-created_time")[:num]
	
#  按月归档模板标签
@register.simple_tag
def archives():
	return Post.objects.dates("created_time", "month", order="DESC")
	
#  分类模板标签
@register.simple_tag
def get_categories():
	return Category.objects.all()
	

