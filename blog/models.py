# blog/models.py
from django.db import models

# Create your models here.

# BLOG MODELS: Post
class Post(models.Model):

	title 	= models.CharField(max_length=63)
	slug 	= models.SlugField()
	text 	= models.TextField()
	pub_date = models.DateField()