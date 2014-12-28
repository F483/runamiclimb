from unidecode import unidecode
from django.db import models
from django.template.defaultfilters import slugify


class Article(models.Model):

  author = models.CharField(max_length=1024)
  title = models.CharField(max_length=1024)
  preview = models.TextField()
  content = models.TextField()
  coverletter = models.TextField()
  featured = models.BooleanField(default=False)
  email = models.EmailField(max_length=1024)
  category = models.ForeignKey(
      "article.Category", 
      related_name="articles", 
      null=True
  )
  issue = models.ForeignKey(
      "article.Issue", 
      related_name="articles", 
      null=True
  )
  gallery = models.ForeignKey(
      "photologue.Gallery", 
      related_name="articles", 
      null=True,
      blank=True
  )

  def title_slug(self):
    return slugify(unidecode(self.title))

  def url(self):
    return "/article/%s/%s.html" % (self.id, self.title_slug())

  def url_edit(self):
    return "/article/edit/%s/%s.html" % (self.id, self.title_slug())

  def url_support(self):
    title_slug = slugify(unidecode(self.title))
    return "/article/support/%s/%s.html" % (self.id, title_slug)

  def __unicode__(self):
    if not self.issue and not self.category:
      return "%s (no issue and category)" % self.title
    if not self.category:
      return "%s (no category)" % self.title
    if not self.issue:
      return "%s (no issue)" % self.title
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
  published = models.BooleanField(default=False)

  def __unicode__(self):
    months = [
        "Jananuary",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    if not self.published:
      return "%s %i (unpublished)" % (months[self.month -1], self.year)
    return "%s %i" % (months[self.month -1], self.year)

  class Meta:

    ordering = ["-year", "-month"]
    #unique_together = (("user", "bounty"),)

