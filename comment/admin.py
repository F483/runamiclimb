from django.contrib import admin
from comment.models import Comment

class CommentAdmin(admin.ModelAdmin):

  list_display = ('alias', 'created', 'relation')

  def relation(self, obj):
    article = obj.article_comments.first()
    if article:
      return "<a href='%s'>%s</a>" % (article.url(), article.title)
    return ""
  relation.allow_tags = True

admin.site.register(Comment, CommentAdmin)

