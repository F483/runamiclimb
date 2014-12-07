from django.contrib import admin

# Register your models here.

from article.models import Article

admin.site.register(Article)


from article.models import Category

admin.site.register(Category)


from article.models import Issue

admin.site.register(Issue)