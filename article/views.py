from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from django.shortcuts import get_object_or_404

def homepage(request):
	articles = Article.objects.all()
	return render(request, 'article/homepage.html', {"articles" : articles })

def displayarticle(request, id):
	article = get_object_or_404(Article, id=id)
	return render(request, 'article/article.html', {"article" : article })

