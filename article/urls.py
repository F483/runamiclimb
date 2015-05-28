from django.conf.urls import patterns, include, url

article_id = r"(?P<article_id>[0-9]+)"
category_slug = r"(?P<category_slug>[a-z0-9\-]+)"
amount = r"(?P<amount>[0-9]+\.[0-9]+)"
ratio = r"(?P<ratio>[0-9]+\.[0-9]+)"

urlpatterns = patterns('article.views',
  
  # submit article view
  url(r"^article/submit\.html$", "submit"),

  # homepage view
  url(r"^$", "listing", { 'category_slug' : None }),
  
  # category view
  url(r"^category/%s/$" % category_slug, "listing"),

  # article view
  url(r"^article/%s/[a-z0-9\-]+\.html$" % article_id, "display"),

  # edit article view
  url(r"^article/edit/%s/[a-z0-9\-]+\.html$" % article_id, "edit"),

  # archive view
  url(r"^archive\.html$", "archive"),

  # site gallery
  url(r"^gallery\.html$", "sitegallery"),

  # retired urls preserved in case of links
  url(r"^article/blog\.html$", "listing", { 'category_slug' : None }),
  url(r"^issue/[0-9]+\-[0-9]+/$", "listing", { 'category_slug' : None }),
  url(r"^issue/[0-9]+\-[0-9]+/category/%s/$" % category_slug, "listing"),
)
