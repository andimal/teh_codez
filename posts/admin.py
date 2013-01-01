from posts.models import Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
	fields = ['title', 'caption', 'tags', 'header_css', 'header', 'proj_loc', 'url', 'github', 'pub_date', 'content']
	list_display = ('title', 'pub_date')
	list_filter = ['pub_date']

admin.site.register(Post, PostAdmin)