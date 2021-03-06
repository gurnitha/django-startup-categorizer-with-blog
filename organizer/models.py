# organizer/models.py
from django.db import models
from django.urls import reverse

# Create your models here.

# ORGANIZER MODELS: Tag
class Tag(models.Model):

	name = models.CharField(
			max_length=31, unique=True)
	slug = models.SlugField(
			unique=True,
			help_text='A label for URL config.')


	def __str__(self):
		return self.name 


	def get_absolute_url(self):
		return reverse('organizer_tag_detail',
			kwargs={'slug': self.slug})
			# args=(self.slug,)) # It is also possible to use args instead of kwargs


# ORGANIZER MODELS: Startup
class Startup(models.Model):

	name = models.CharField(
			max_length=31,
			db_index=True)
	slug = models.SlugField(
			max_length=31,
			unique=True,
			help_text='A label for URL config.')
	description = models.TextField()
	founded_date = models.DateField(
			'date founded')
	contact = models.EmailField(
			max_length=225)
	website = models.URLField()
	# ManyToMany Rel: 
	## A Startup may have many tags
	## A tag may belongs to many startup
	tags = models.ManyToManyField(Tag)


	class Meta:
		ordering 	  = ['name']
		get_latest_by = 'founded_date'


	def __str__(self):
		return self.name 
		

	def get_absolute_url(self):
		return reverse('organizer_startup_detail',
			kwargs={'slug': self.slug})



# ORGANIZER MODELS: NewsLink
class NewsLink(models.Model):

	title = models.CharField(
			max_length=63)
	pub_date = models.DateField(
			'date published')
	link = models.URLField(
			max_length=225)
	# OneToMany Rel: 
	## A startup may have many newslink
	startup = models.ForeignKey(
			Startup,
			on_delete=models.CASCADE)


	class Meta:
		verbose_name  = 'news article'
		ordering 	  = ['-pub_date']
		get_latest_by = 'pub_date'


	def __str__(self):
		return "{}:{}".format(
			self.startup, self.title)

