from django.contrib import admin
from article.models import Article, Category, Issue


class ArticleAdmin(admin.ModelAdmin):

  list_display = (
    'title', 'author', 'email',
    'issue', 'category', 'ordering_category',
    'featured', 'ordering_featured'
  )
  fieldsets = [
    ('Article content', {'fields': ['title', 'preview', 'content', 'gallery']}),
    ('Author info',     {'fields': ['author', 'email', 'coverletter']}),
    ('Publishing info', {
      'fields': [
        'issue',
        'category', 'ordering_category',
        'featured', 'ordering_featured'
      ]
    }),
  ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Issue)
