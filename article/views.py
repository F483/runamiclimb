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

def homepage(request):
  return listarticles(request, None, None, None)

def issue(request, year, month):
  return listarticles(request, None, year, month)

def submit(request):
  categories = Category.objects.all()
  issues = Issue.objects.all()

  if request.method == "POST":
    form = forms.Submit(request.POST)
    if form.is_valid():
      article = Article()
      article.title = form.cleaned_data["title"].strip()
      article.author = form.cleaned_data["author"].strip()
      article.email = form.cleaned_data["email"].strip()
      article.content = form.cleaned_data["content"]
      article.date = datetime.date.today()
      article.save()
      return HttpResponseRedirect("/")
  else: # "GET"
    form = forms.Submit()

  templatearguments = {
    "categories" : categories,
    "issues" : issues,
    "form" : form,
    "cancel_url" : "/",
    "title" : "Submit Article"
  }
  return render(request, 'article/submit.html', templatearguments)

def edit(request, id):
  if not request.user.is_superuser:
    raise PermissionDenied

  article = get_object_or_404(Article, id=id)
  categories = Category.objects.all()
  issues = Issue.objects.all()

  if request.method == "POST":
    form = forms.Edit(request.POST, article=article)
    if form.is_valid():
      article.title = form.cleaned_data["title"].strip()
      article.author = form.cleaned_data["author"].strip()
      article.email = form.cleaned_data["email"].strip()
      article.content = form.cleaned_data["content"]
      article.save()
      return HttpResponseRedirect(article.url())
  else: # "GET"
    form = forms.Edit(article=article)

  templatearguments = {
    "categories" : categories,
    "issues" : issues,
    "form" : form,
    "cancel_url" : "/",
    "title" : "Edit Article"
  }
  return render(request, 'article/submit.html', templatearguments)




def listarticles(request, category_slug, year, month):
  articles = Article.objects.all()
  categories = Category.objects.all()
  issues = Issue.objects.all()

  currentcategory = None
  if not category_slug:
    articles = articles.filter(featured=True)
  else:
    for category in categories:
      if category.slug() == category_slug:
        currentcategory = category
    if not currentcategory:
      raise Http404
    articles = articles.filter(category=currentcategory)

  currentissue = None
  if month and year:
    currentissue = get_object_or_404(Issue, month=int(month), year=int(year))
  else:
    currentissue = Issue.objects.all()[0]
  articles = articles.filter(issue=currentissue)

  templatearguments = {
    "articles" : articles,
    "categories" : categories,
    "issues" : issues,
    "currentcategory" : currentcategory,
    "currentissue" : currentissue,
  }
  return render(request, 'article/homepage.html', templatearguments)

def displayarticle(request, id):
  article = get_object_or_404(Article, id=id)
  categories = Category.objects.all()
  issues = Issue.objects.all()
  currentissue = article.issue
  currentcategory = article.category
  templatearguments = {
    "article" : article,
    "categories" : categories,
    "issues" : issues,
    "currentcategory" : currentcategory,
    "currentissue" : currentissue,
  }
  return render(request, 'article/article.html', templatearguments)

