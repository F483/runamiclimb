from django.db import models

# Create your models here.

class Article(models.Model):

  title = models.CharField(max_length=1024)
  author = models.CharField(max_length=1024)
  date = models.DateField()
  preview = models.TextField()
  content = models.TextField()
  def url(self):
  	return "/article/%s/%s.html" % (self.id, "todo-title-slug")

