import datetime
from unidecode import unidecode
from django.db import models
from django.template.defaultfilters import slugify


class Article(models.Model):

  # Article content
  title = models.CharField(max_length=1024)
  preview = models.TextField()
  content = models.TextField()
  gallery = models.ForeignKey(
      "photologue.Gallery",
      related_name="articles",
      null=True,
      blank=True
  )

  # Author info
  author = models.CharField(max_length=1024)
  email = models.EmailField(max_length=1024)
  coverletter = models.TextField()

  # Category info
  category = models.ForeignKey(
      "article.Category",
      related_name="articles",
      null=True,
      blank=True
  )
  featured = models.BooleanField(default=False)
  blog = models.BooleanField(default=False)
  date = models.DateField(null=True, default=None, blank=True)

  # User content
  comments = models.ManyToManyField(
      'comment.Comment', related_name="article_comments", null=True, blank=True
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
    if not self.category:
      return "%s (no category)" % self.title
    return self.title

  def published(self):
    today = datetime.datetime.now().date()
    return (self.date and (today >= self.date))

  class Meta:
    ordering = ["-date"]

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
  pdf = models.FileField(upload_to="issues", null=True, default=None)
  gallery = models.ForeignKey( # for issue cover and index images
      "photologue.Gallery",
      related_name="issues",
      null=True,
      blank=True
  )

  def __unicode__(self):
    months = [
        "January",
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

