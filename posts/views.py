from django.shortcuts import render_to_response, get_object_or_404

from posts.models import Post
from tagging.models import Tag, TaggedItem
from tagging.fields import TagField

from django.http import HttpResponse
from django.template import RequestContext
from operator import itemgetter

def home(request):
	latest_post_list = Post.objects.all().order_by('-pub_date')
	
	#get list of all tags & their count
	tag_list = []
	for t in Tag.objects.cloud_for_model(Post):
		ind = []
		ind.append(t.name)
		ind.append(t.count)
		tag_list.append(ind)

	return render_to_response('posts/index.html', {
		'latest_post_list': latest_post_list,
		#send over list of tags, sorted by most used tag first
		'tag_list': sorted(tag_list, key=itemgetter(1), reverse=True)
	}, context_instance=RequestContext(request))

def detail(request, post_url):
	p = get_object_or_404(Post, url=post_url)
	return render_to_response('posts/detail.html', {'post': p})