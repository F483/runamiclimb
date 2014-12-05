from django.conf.urls import patterns, include, url

urlpatterns = patterns('article.views',
	url(r"^$", "homepage"),
)
