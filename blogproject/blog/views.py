from django.shortcuts import render

# Create your views here.
def index(request):
	context = { "title": "This is blog", "body": "我正在学习Python, Django框架......" }
	return render(request, "blog/index.html", context=context)