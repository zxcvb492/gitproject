from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm

# Create your views here.
def post_comment(request, post_pk):
	post = get_object_or_404( Post, pk=post_pk )
	
	if request.method == 'POST':
		form = CommentForm( request.POST )
		
		if form.is_valid():
			comment = form.save( commit=False )
			comment.post = post
			comment.save()
			return redirect(post)
		else:
			#  获取该篇文章 post 下所有评论
			comment_list = post.comment_set.all()
			context = { 'post': post,
			                    'form': form,
			                    'comment_list': comment_list
			                    }
			return render(request, 'blog/detail.html', context=content)
			
	#  不是 POST 请求, 没有提交数据, 重定向到文章详情页
	return redirect(post)
			