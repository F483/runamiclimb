# -*- coding: utf-8 -*-
# Copyright (c) 2014 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE.TXT file)

from article.models import Category, Issue

def add_issues(request):
  issues = Issue.objects.all()
  if not request.user.is_superuser:
    issues = issues.filter(published=True)
  currentissue = len(issues) and issues[0] or None
  return { 'issues': issues, 'currentissue': currentissue }

def add_categories(request):
  return { 'categories': Category.objects.all() }
