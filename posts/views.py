from django.shortcuts import render_to_response, get_object_or_404
from posts.models import Post
from django.http import HttpResponse
from django.template import RequestContext

def home(request):
	latest_post_list = Post.objects.all().order_by('-pub_date')[:5]
	return render_to_response('posts/index.html', {
		'latest_post_list': latest_post_list
	}, context_instance=RequestContext(request))

def detail(request, post_url):
	p = get_object_or_404(Post, url=post_url)
	return render_to_response('posts/detail.html', {'post': p})