from django.db import models
from tagging.fields import TagField
from tagging.models import Tag
from ckeditor.fields import RichTextField

class Post(models.Model):
	title 		= models.CharField(max_length=50)
	caption 	= models.CharField(max_length=200)
	header_css 	= models.TextField()
	header 		= models.CharField(max_length=50)
	proj_loc 	= models.CharField(max_length=50)
	url 		= models.SlugField()
	github		= models.CharField(max_length=200)
	pub_date 	= models.DateTimeField('date published')
	tags 		= TagField()
	content 	= RichTextField(config_name='content_ckeditor')

	def get_tags(self):
		return Tag.objects.get_for_object(self)

	def __unicode__(self):
		return self.title