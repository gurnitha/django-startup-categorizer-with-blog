from django.shortcuts import render
from .models import Tag

# Create your views here.

# Homepage (tag_list) view
def homepage(request):
	tag_list = Tag.objects.all()
	context = {
		'tag_list': tag_list
	}
	return render(request, 'organizer/tag_list.html', context)


# Tag detail page
def tag_detail(request, slug):
	# slug = ?
	tag = Tag.objects.get(slug__iexact=slug)
	context = {
		'tag': tag
	}
	return render(request, 'organizer/tag_detail.html', context)
