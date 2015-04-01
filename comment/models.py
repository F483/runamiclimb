from django.db import models

class Comment(models.Model):

  alias = models.CharField(max_length=512, blank=True)
  content = models.TextField()
  created = models.DateTimeField(auto_now_add=True)

  def url_delete(self):
    return "/comment/delete/%i" % self.id

  class Meta:

    ordering = ["created"]

