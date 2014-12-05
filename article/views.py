from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article

def homepage(request):
	articles = Article.objects.all()
	return render(request, 'article/homepage.html', {"articles" : articles })

