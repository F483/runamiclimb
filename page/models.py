from unidecode import unidecode
from django.db import models
from django.template.defaultfilters import slugify

class Page(models.Model):

  # Page content
  title = models.CharField(max_length=1024)
  content = models.TextField()

  # Sidebar info
  in_sidebar = models.BooleanField(default=False)
  sidebar_ordering = models.IntegerField(default=0)

  def title_slug(self):
    return slugify(unidecode(self.title))

  def url(self):
    return "/page/%s/%s.html" % (self.id, self.title_slug())

  def url_edit(self):
    return "/page/edit/%s/%s.html" % (self.id, self.title_slug())

  def url_delete(self):
    return "/page/delete/%s/%s.html" % (self.id, self.title_slug())

  def __unicode__(self):
    return self.title
