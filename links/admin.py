from django.contrib import admin
from links.models import Link

class LinkAdmin(admin.ModelAdmin):

  list_display = ('title', 'url', 'in_sidebar', 'sidebar_ordering')
  fieldsets = [
    ('Page content', {'fields': ['title', 'url']}),
    ('Sidebar info', {'fields': ['in_sidebar', 'sidebar_ordering']}),
  ]


admin.site.register(Link, LinkAdmin)
