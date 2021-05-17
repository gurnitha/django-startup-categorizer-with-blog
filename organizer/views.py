from django.shortcuts import render, get_object_or_404
from .models import Startup, Tag

# Create your views here.

# Startup List
def startup_list(request):
	startup_list = Startup.objects.all()
	context = {
		'startup_list': startup_list
	}
	return render(request,'organizer/startup_list.html', context)


# Startup Detail
def startup_detail(request, slug):
	startup = get_object_or_404(Startup, slug__iexact=slug)
	context = {
		'startup': startup
	}
	return render(request,'organizer/startup_detail.html', context)



# Tag detail page
def tag_detail(request, slug):
	# slug = ?
	tag = get_object_or_404(Tag, slug__iexact=slug)
	context = {
		'tag': tag
	}
	return render(request, 'organizer/tag_detail.html', context)


# Homepage (tag_list) view
def homepage(request):
	tag_list = Tag.objects.all()
	context = {
		'tag_list': tag_list
	}
	return render(request, 'organizer/tag_list.html', context)






def tag_detail(request, slug):
    tag = get_object_or_404(
        Tag, slug__iexact=slug)
    return render(
        request,
        'organizer/tag_detail.html',
        {'tag': tag})
def tag_list(request):
    return render(
        request,
        'organizer/tag_list.html',
        {'tag_list': Tag.objects.all()})