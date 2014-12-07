from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from article.models import Category
from article.models import Issue
from django.shortcuts import get_object_or_404

def homepage(request):
	articles = Article.objects.filter(featured=True)
	categories = Category.objects.all()
	issues = Issue.objects.all()
	return render(request, 'article/homepage.html', {"articles" : articles, "categories" : categories, "issues" : issues})



def displayarticle(request, id):
	article = get_object_or_404(Article, id=id)
	categories = Category.objects.all()
	issues = Issue.objects.all()
	return render(request, 'article/article.html', {"article" : article, "categories" : categories, "issues" : issues})

