from django.conf.urls import patterns, include, url

article_id = r"(?P<article_id>[0-9]+)"
year = r"(?P<year>[0-9]+)"
month = r"(?P<month>[0-9]+)"
category_slug = r"(?P<category_slug>[a-z0-9\-]+)"
amount = r"(?P<amount>[0-9]+\.[0-9]+)"
ratio = r"(?P<ratio>[0-9]+\.[0-9]+)"

urlpatterns = patterns('article.views',
  
  # homepage view
  url(
    r"^$", 
    "listing",
    { 'year' : None, 'month' : None, 'category_slug' : None }
  ),

  # issue view
  url(
    r"^issue/%s\-%s/$" % (year, month), 
    "listing",
    { 'category_slug' : None}
  ),

  # issue category view
  url(
    r"^issue/%s\-%s/category/%s/$" % (year, month, category_slug), 
    "listing"
  ),

  # article view
  url(r"^article/%s/[a-z0-9\-]+\.html$" % article_id, "display"),

  # edit article view
  url(r"^article/edit/%s/[a-z0-9\-]+\.html$" % article_id, "edit"),

  # submit article view
  url(r"^article/submit.html$", "submit"),

  # article submited
  url(r"^article/submitted.html$", "submitted"),

  # contact page
  url(r"^article/contact.html$", "contact"),

)
