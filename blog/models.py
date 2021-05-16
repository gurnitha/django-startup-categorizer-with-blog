# blog/models.py
from django.db import models
from organizer.models import Startup, Tag

# Create your models here.

# BLOG MODELS: Post
class Post(models.Model):

	title 	= models.CharField(max_length=63)
	slug 	= models.SlugField()
	text 	= models.TextField()
	pub_date= models.DateField()
	# ManyToMany Rel:
	## A post may have many tags
	## A tag may belongs to many posts
	tags 	= models.ManyToManyField(Tag)
	# ManyToMany Rel:
	## A startup may posting many posts
	## A post may belongs to many startup
	startups= models.ManyToManyField(Startup)