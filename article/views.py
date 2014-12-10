import datetime
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from article.models import Category
from article.models import Issue
from article import forms
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied

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
      return HttpResponseRedirect("/")
  else: # "GET"
    form = forms.Submit()

  templatearguments = {
    "form" : form,
    "cancel_url" : "/",
    "title" : "Submit Article",
    "currentissue" : Issue.objects.all()[0],
  }
  return render(request, 'article/submit.html', templatearguments)

def edit(request, article_id):
  if not request.user.is_superuser:
    raise PermissionDenied

  article = get_object_or_404(Article, id=article_id)
  currentissue = article.issue and article.issue or Issue.objects.all()[0]
  currentcategory = article.category and article.category or None

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
      article.featured = form.cleaned_data["featured"]
      article.save()
      return HttpResponseRedirect(article.url())
  else: # "GET"
    form = forms.Edit(article=article)

  templatearguments = {
    "currentissue" : currentissue,
    "currentcategory" : currentcategory,
    "form" : form,
    "cancel_url" : article.url(),
    "title" : "Edit Article",
  }
  return render(request, 'article/submit.html', templatearguments)

def listing(request, category_slug, year, month):
  articles = Article.objects.all()

  # issue
  currentissue = None
  if month and year: # show articles from selected issue
    currentissue = get_object_or_404(Issue, month=int(month), year=int(year))
  else: # show articles from newest issue
    currentissue = Issue.objects.all()[0]
  if not currentissue.published and not request.user.is_superuser:
    raise PermissionDenied
  articles = articles.filter(issue=currentissue)

  # category
  currentcategory = None
  if not category_slug: # show featured articles
    articles = articles.filter(featured=True)
  else: # show category articles
    for category in Category.objects.all():
      if category.slug() == category_slug:
        currentcategory = category
    if not currentcategory:
      raise Http404
    articles = articles.filter(category=currentcategory)

  left_articles, right_articles = [ articles[i::2] for i in xrange(2) ]
  templatearguments = {
    "left_articles" : left_articles,
    "right_articles" : right_articles,
    "currentcategory" : currentcategory,
    "currentissue" : currentissue,
  }
  return render(request, 'article/listing.html', templatearguments)

def display(request, article_id):
  article = get_object_or_404(Article, id=article_id)
  currentissue = article.issue
  currentcategory = article.category
  if not currentissue.published and not request.user.is_superuser:
    raise PermissionDenied
  templatearguments = {
    "article" : article,
    "currentcategory" : currentcategory,
    "currentissue" : currentissue,
  }
  return render(request, 'article/display.html', templatearguments)

