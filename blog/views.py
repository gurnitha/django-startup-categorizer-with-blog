from django.shortcuts import render

# Create your views here.

from .models import Post


def post_list(request):
	post_list = Post.objects.all()
	context = {
		'post_list':post_list
	}
	return render(request, 'blog/post_list.html',context)