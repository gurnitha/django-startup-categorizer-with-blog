# # blog/views.py
# from django.shortcuts import render, get_object_or_404

# # Create your views here.

# from .models import Post


# # Post List
# # http://127.0.0.1:8000/blog/
# def post_list(request):
# 	post_list = Post.objects.all()
# 	context = {
# 		'post_list':post_list
# 	}
# 	return render(request, 'blog/post_list.html',context)


# # Post Detail: 
# # http://127.0.0.1:8000/blog/2021/05/flask-essentials/
# def post_detail(request, year, month, slug):
# 	post = get_object_or_404(
# 			Post,
# 			pub_date__year=year,
# 			pub_date__month=month,
# 			slug=slug)
# 	context = {
# 		'post':post
# 	}
# 	return render(request, 'blog/post_detail.html',context)  


# USING CLASS-BASED VIEWS

# blog/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

# Create your views here.

from .models import Post


# Post List
# http://127.0.0.1:8000/blog/
class PostList(View):
	
	template_name = 'blog/post_list.html'

	def get(self, request):
		post_list = Post.objects.all()
		context = {
			'post_list':post_list
		}

		return render(request, self.template_name, context)


# Post Detail: 
# http://127.0.0.1:8000/blog/2021/05/flask-essentials/
def post_detail(request, year, month, slug):
	post = get_object_or_404(
			Post,
			pub_date__year=year,
			pub_date__month=month,
			slug=slug)
	context = {
		'post':post
	}
	return render(request, 'blog/post_detail.html',context)  


