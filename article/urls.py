from django.conf.urls import patterns, include, url

urlpatterns = patterns('article.views',
  url(r"^$", "homepage"),

  url(r"^issue/(?P<year>[0-9]+)\-(?P<month>[0-9]+)/category/(?P<category_slug>[a-z0-9\-]+)/", "listarticles"),
  url(r"^issue/(?P<year>[0-9]+)\-(?P<month>[0-9]+)/", "issue"),
  url(r"^article/(?P<id>[0-9]+)/[a-z0-9\-]+\.html$", "displayarticle"),
  url(r"^article/submit.html$", "submit"),
  url(r"^article/edit/(?P<id>[0-9]+)/[a-z0-9\-]+\.html$", "edit"),

)
