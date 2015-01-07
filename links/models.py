from django.db import models

class Link(models.Model):

  # Page content
  title = models.CharField(max_length=1024)
  url = models.URLField(max_length=1024)
  # TODO icon

  # Sidebar info
  in_sidebar = models.BooleanField(default=False)
  sidebar_ordering = models.IntegerField(default=0)

  def __unicode__(self):
    return self.title

