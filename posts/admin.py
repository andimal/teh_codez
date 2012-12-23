from posts.models import Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
	fields = ['title', 'caption', 'tags', 'proj_loc', 'pub_date']
	list_display = ('title', 'pub_date')
	list_filter = ['pub_date']

admin.site.register(Post, PostAdmin)