# organizer/models.py
from django.db import models

# Create your models here.

# ORGANIZER MODELS: Tag
class Tag(models.Model):

	name = models.CharField(max_length=31)
	slug = models.SlugField()


# ORGANIZER MODELS: Startup
class Startup(models.Model):

	name = models.CharField(max_length=31)
	slug = models.SlugField()
	description = models.TextField()
	founded_date = models.DateField()
	contact = models.EmailField()
	website = models.URLField()


# ORGANIZER MODELS: NewsLink
class NewsLink(models.Model):
	
	title = models.CharField(max_length=63)
	pub_date = models.DateField()
	link = models.URLField()

