from unidecode import unidecode                                                                                 
from django.db import models
from django.template.defaultfilters import slugify                               

# Create your models here.

class Article(models.Model):

  title = models.CharField(max_length=1024)
  author = models.CharField(max_length=1024)
  date = models.DateField()
  preview = models.TextField()
  content = models.TextField()
  category = models.ForeignKey("article.Category", related_name="articles", null=True)
  featured = models.BooleanField(default=False)
  issue = models.ForeignKey("article.Issue", related_name="articles", null=True)

  def url(self):
    return "/article/%s/%s.html" % (self.id, "todo-title-slug")

  def __unicode__(self):
    return self.title


class Category(models.Model):

  title = models.CharField(max_length=1024)

  def slug(self):
    return slugify(unidecode(self.title)) 

  def __unicode__(self):
    return self.title


class Issue(models.Model):

  month = models.IntegerField()
  year = models.IntegerField()

  def __unicode__(self):
    return "%i - %i" % (self.year, self.month)
    
  class Meta:

    ordering = ["-year", "-month"]
    #unique_together = (("user", "bounty"),)

