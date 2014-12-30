from django.contrib import admin
from comment.models import Comment

class CommentAdmin(admin.ModelAdmin):

  list_display = ('alias', 'created')

admin.site.register(Comment, CommentAdmin)

