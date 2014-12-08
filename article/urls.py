from django.conf.urls import patterns, include, url

urlpatterns = patterns('article.views',
	url(r"^$", "homepage"),
  url(r"^articles/(?P<category_title>[a-z]+)/(?P<year>[0-9]+)\-(?P<month>[0-9]+)/", "listarticles"),
	url(r"^article/(?P<id>[0-9]+)/[a-z0-9\-]+\.html$", "displayarticle"),
)
