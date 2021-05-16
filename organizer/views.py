from django.shortcuts import render
from .models import Tag
# Create your views here.

def homepage(request):
	tag_list = Tag.objects.all()
	context = {
		'tag_list': tag_list
	}
	return render(request, 'organizer/tag_list.html', context)
