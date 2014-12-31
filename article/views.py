import datetime
import uuid
from decimal import Decimal
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from config import settings
from support.forms import Support
from article.models import Article, Category, Issue
from page.models import Page
from article import forms
from comment import forms as comment_forms
from comment import models as comment_models

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
      submitted_page = get_object_or_404(Page, title="Article Submitted")
      return HttpResponseRedirect(submitted_page.url())
  else: # "GET"
    form = forms.Submit()

  guidelines = get_object_or_404(Page, title="Submission Guidelines")
  templatearguments = {
    "generic_form" : {
      "title" : "Submit Article",
      "markdown_info" : guidelines.content,
      "form" : form,
      "cancel_url" : "/",
    }
  }
  return render(request, 'common/submit.html', templatearguments)

@login_required
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
    "generic_form" : {
      "title" : "Edit Article",
      "cancel_url" : article.url(),
      "form" : form,
    }
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
    support_form = Support(request.POST)
    comment_form = comment_forms.Comment(request.POST)

    if comment_form.is_valid():
      comment = comment_models.Comment()
      comment.alias = comment_form.cleaned_data["alias"].strip()
      comment.content = comment_form.cleaned_data["content"].strip()
      comment.save()
      article.comments.add(comment)
      return HttpResponseRedirect(article.url())

    if support_form.is_valid():
      amount = support_form.cleaned_data["amount"]
      ratio = support_form.cleaned_data["ratio"] / Decimal("100.0")
      url = "/support/%s/%.2f/%.2f/%s.html" % (
          article.id, amount, ratio, article.title_slug()
      )
      return HttpResponseRedirect(url)

  else: # "GET"
    support_form = Support()
    comment_form = comment_forms.Comment()

  templatearguments = {
    "article" : article,
    "currentcategory" : article.category,
    "currentissue" : article.issue,

    "comment_form" : {
      "title" : "Create comment",
      'form' : comment_form,
      "submit_label" : "Post comment",
      'submit_class' : "btn btn-success",
    },

    "support_form" : {
      "title" : "Support the author",
      'form' : support_form,
      "submit_label" : "Continue",
      'submit_class' : "btn btn-success",
    },
  }
  return render(request, 'article/display.html', templatearguments)

