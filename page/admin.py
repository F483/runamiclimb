from django.contrib import admin
from page.models import Page

class PageAdmin(admin.ModelAdmin):

  list_display = ('title', 'in_sidebar', 'sidebar_ordering')
  fieldsets = [
    ('Page content', {'fields': ['title', 'content']}),
    ('Sidebar info', {'fields': ['in_sidebar', 'sidebar_ordering']}),
  ]


admin.site.register(Page, PageAdmin)
