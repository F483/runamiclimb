from django.conf.urls import patterns, include, url

article_id = r"(?P<article_id>[0-9]+)"
amount = r"(?P<amount>[0-9]+\.[0-9]+)"
ratio = r"(?P<ratio>[0-9]+\.[0-9]+)"

urlpatterns = patterns('support.views',

  url(
    r"^%s/%s/%s/[a-z0-9\-]+\.html$" % (
      article_id, amount, ratio
    ), 
    "support"
  ),

  url(
    r"^thanks/%s/[a-z0-9\-]+\.html$" % article_id, 
    "paypal_return",
    { 'template' : "support/thanks.html"}
  ),

  url(
    r"^cancel/%s/[a-z0-9\-]+\.html$" % article_id, 
    "paypal_return",
    { 'template' : "support/cancel.html"}
  ),

)
