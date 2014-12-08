from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from article.models import Category
from article.models import Issue
from django.shortcuts import get_object_or_404


def homepage(request):
    return listarticles(request, None, None, None)


def listarticles(request, category_title, month, year):
    articles = Article.objects.all()

    currentcategory = None
    if not category_title:
        articles = articles.filter(featured=True)
    else:
        currentcategory = get_object_or_404(Category, title=category_title)
        articles = articles.filter(category=currentcategory)

    currentissue = None
    if month and year:
        currentissue = get_object_or_404(Issue, month=int(month), year=int(year))
    else:
        currentissue = Issue.objects.all()[0]
    articles = articles.filter(issue=currentissue)

    categories = Category.objects.all()
    issues = Issue.objects.all()
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

