from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=50)
	caption = models.CharField(max_length=200)
	tags = models.CharField(max_length=200)
	proj_loc = models.CharField(max_length=50)
	url = models.CharField(max_length=50)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.title