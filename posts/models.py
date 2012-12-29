from django.db import models
from tagging.fields import TagField
from tagging.models import Tag

class Post(models.Model):
	title = models.CharField(max_length=50)
	caption = models.CharField(max_length=200)
	proj_loc = models.CharField(max_length=50)
	url = models.SlugField()
	pub_date = models.DateTimeField('date published')
	tags = TagField()
	content = models.TextField()

	def get_tags(self):
		return Tag.objects.get_for_object(self)

	def __unicode__(self):
		return self.title