import datetime
import uuid
from decimal import Decimal
from django.shortcuts import render
from article.models import Article, Category, Issue
from article import forms
from support.forms import Support
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from paypal.standard.forms import PayPalPaymentsForm
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from config import settings


SUBMISSION_GUIDLINES = """
#### Submission Guidlines

Thank you for submitting to Trainless Magazine. We look forward to reading
your work.

We accept nonfiction and fiction writing. Please read through our magazine to
familiarize yourself with what kind of work we publish. Nonfiction articles
should stay relevant to our magazine's theme of travel, athleticism, and
culture. Fiction is much more open, as every world created through fiction
presents a new "culture." 

Stories ranging from 100-3,000 words are accepted. It would have to be an
incredible, really unstoppable story to keep our readers reading after 3,000
words. 

In regards to format, words that are italicized should have this symbol * at
the start and end of the italicized word or phrase. Bold letters should be
typed in all capital letters.

In terms of style, excessive profanity, violence, and erotica will not be
accepted.

Poetry is, at this time, not accepted.

Please send a maximum of two submissions to be considered per issue. We print
between 10 and 15 articles a month, depending on length, and only one article
or story per author per issue. 

Please allow two to four weeks response time.

Relevant photographs will be requested upon acceptance of the article or story.

Simultaneous articles are accepted. We ask that you tell us as soon as your
work is accepted elsewhere.
"""

def submit(request):

  if request.method == "POST":
    form = forms.Submit(request.POST)
    if form.is_valid():
      article = Article()
      article.title = form.cleaned_data["title"].strip()
      article.author = form.cleaned_data["author"].strip()
      article.email = form.cleaned_data["email"].strip()
      article.content = form.cleaned_data["content"]
      article.coverletter = form.cleaned_data["coverletter"]
      article.save()
      return HttpResponseRedirect("/article/submitted.html")
  else: # "GET"
    form = forms.Submit()

  templatearguments = {
    "form" : form,
    "form_info" : SUBMISSION_GUIDLINES,
    "form_cancel_url" : "/",
    "form_title" : "Submit Article",
  }
  return render(request, 'common/submit.html', templatearguments)

def submitted(request):
  return render(request, 'article/submitted.html', {})

def edit(request, article_id):
  if not request.user.is_superuser:
    raise PermissionDenied

  article = get_object_or_404(Article, id=article_id)

  if request.method == "POST":
    form = forms.Edit(request.POST, article=article)
    if form.is_valid():
      article.title = form.cleaned_data["title"].strip()
      article.author = form.cleaned_data["author"].strip()
      article.preview = form.cleaned_data["preview"]
      article.content = form.cleaned_data["content"]
      article.coverletter = form.cleaned_data["coverletter"]
      article.issue = form.cleaned_data["issue"]
      article.category = form.cleaned_data["category"]
      article.ordering_category = form.cleaned_data["ordering_category"]
      article.featured = form.cleaned_data["featured"]
      article.ordering_featured = form.cleaned_data["ordering_featured"]
      article.save()
      return HttpResponseRedirect(article.url())
  else: # "GET"
    form = forms.Edit(article=article)

  templatearguments = {
    "form" : form,
    "form_cancel_url" : article.url(),
    "form_title" : "Edit Article",
  }
  return render(request, 'common/submit.html', templatearguments)

def listing(request, category_slug, year, month):
  articles = Article.objects.all()

  # issue
  currentissue = None
  if month and year: # show articles from selected issue
    currentissue = get_object_or_404(Issue, month=int(month), year=int(year))
  else: # show articles from newest published issue
    issues = Issue.objects.filter(published=True)
    currentissue = issues and issues[0] or None
  if currentissue and not currentissue.published and not request.user.is_superuser:
    raise PermissionDenied
  articles = articles.filter(issue=currentissue)

  # category
  currentcategory = None
  if not category_slug: # show featured articles
    articles = articles.filter(featured=True)
    articles = articles.order_by('ordering_featured')
  else: # show category articles
    for category in Category.objects.all():
      if category.slug() == category_slug:
        currentcategory = category
    if not currentcategory:
      raise Http404
    articles = articles.filter(category=currentcategory)
    articles = articles.order_by('ordering_category')
  
  middle = len(articles) / 2
  middle = (len(articles) % 2 != 0) and (middle + 1) or middle
  templatearguments = {
    "left_articles" : articles[:middle],
    "right_articles" : articles[middle:],
    "currentcategory" : currentcategory,
    "currentissue" : currentissue,
  }
  return render(request, 'article/listing.html', templatearguments)

def display(request, article_id):
  article = get_object_or_404(Article, id=article_id)
  if not article.issue.published and not request.user.is_superuser:
    raise PermissionDenied

  if request.method == "POST":
    form = Support(request.POST)
    if form.is_valid():
      amount = form.cleaned_data["amount"]
      ratio = form.cleaned_data["ratio"] / Decimal("100.0")
      url = "/support/%s/%.2f/%.2f/%s.html" % (
          article.id, amount, ratio, article.title_slug()
      )
      return HttpResponseRedirect(url)
  else: # "GET"
    form = Support()

  templatearguments = {
    "form_title" : "Support the author",
    "submit_label" : "Continue",
    "submit_button_class" : "btn btn-success",
    "form" : form,
    "article" : article,
    "currentcategory" : article.category,
    "currentissue" : article.issue,
  }
  return render(request, 'article/display.html', templatearguments)

def contact(request):
  return render(request, 'common/contact.html', {})

