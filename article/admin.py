from django.contrib import admin
from article.models import Article, Category, Issue


class ArticleAdmin(admin.ModelAdmin):

  list_display = (
    'title', 
    'author', 
    'email',
    'category',
    'featured',
    'blog',
    'date'
  )
  fieldsets = [
    ('Article content', {'fields': ['title', 'preview', 'content', 'gallery']}),
    ('Author info',     {'fields': ['author', 'email', 'coverletter']}),
    ('Publishing info', {'fields': ['category', 'featured', 'blog', 'date'] }),
  ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Issue)
