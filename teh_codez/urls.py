from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'posts.views.home', name='home'),
    url(r'^posts/(?P<post_url>\w+)/$', 'posts.views.detail', name='detail_view'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
)