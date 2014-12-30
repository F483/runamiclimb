from django.conf.urls import patterns, include, url

comment_id = r"(?P<comment_id>[0-9]+)"

urlpatterns = patterns('comment.views',
  url(r"^delete/%s$" % comment_id, "delete"),
)

