from django.contrib import admin
from article.models import Article, Category, Issue


class ArticleAdmin(admin.ModelAdmin):

  list_display = (
    'title', 'author', 'email',
    'issue', 'category',
    'featured',
    'blog_article'
  )
  fieldsets = [
    ('Article content', {'fields': ['title', 'preview', 'content', 'gallery']}),
    ('Author info',     {'fields': ['author', 'email', 'coverletter']}),
    ('Publishing info', {'fields': ['issue', 'category', 'featured'] }),
    ('Blog info', { 'fields': [ 'blog_article', 'blog_date' ] }),
  ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Issue)
