# -*- coding: utf-8 -*-
# Copyright (c) 2014 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE.TXT file)

from django.conf import settings as _settings
from article.models import Category
from article.models import Issue
from photologue.models import Gallery
from photologue.models import PhotoSize

def add_settings(request):
  return { 'settings': _settings }

def add_issues(request):
  issues = Issue.objects.all()
  if not request.user.is_superuser:
    issues = issues.filter(published=True)
  currentissue = len(issues) and issues[0] or None
  return { 'issues': issues, 'currentissue': currentissue }

def add_categories(request):
  return { 'categories': Category.objects.all() }

def add_titlebar_photos(request):
  galleries = Gallery.objects.filter(title="Titlebar photos")
  sizes = PhotoSize.objects.filter(name="titlebar_photo")
  if galleries and sizes:
    return { 
        'titlebar_photos' : galleries[0].photos.all()[:5],
        'titlebar_photo_size' : sizes[0]
    }
  return { 'titlebar_photos' : [], 'titlebar_photo_size' : None }
