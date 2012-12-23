from django.shortcuts import render_to_response
from posts.models import Post
from django.http import HttpResponse

def home(request):
	latest_post_list = Post.objects.all().order_by('-pub_date')[:5]
	return render_to_response('posts/index.html', {'latest_post_list': latest_post_list})