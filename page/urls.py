from django.conf.urls import patterns, include, url

page_id = r"(?P<page_id>[0-9]+)"

urlpatterns = patterns('page.views',
  url(r"^create.html$", "create"),
  url(r"^%s/[a-z0-9\-]+\.html$" % page_id, "display"),
  url(r"^edit/%s/[a-z0-9\-]+\.html$" % page_id, "edit"),
  url(r"^delete/%s/[a-z0-9\-]+\.html$" % page_id, "delete"),
)

