from django.conf.urls import patterns, include, url

urlpatterns = patterns('article.views',
	url(r"^$", "homepage"),
	url(r"^/article/(?P<id>[0-9]+)/[a-z0-9\-]+\.html$", "displayarticle"),
)
