from django.db import models

# Create your models here.

class Article(models.Model):

  title = models.CharField(max_length=1024)
  author = models.CharField(max_length=1024)
  date = models.DateField()
  preview = models.TextField()
  content = models.TextField()
  category = models.ForeignKey("article.Category", related_name="articles", null=True)
  def url(self):
  	return "/article/%s/%s.html" % (self.id, "todo-title-slug")

  def __unicode__(self):
  	return self.title



class Category(models.Model):

  title = models.CharField(max_length=1024)
  def __unicode__(self):
  	return self.title
  	
