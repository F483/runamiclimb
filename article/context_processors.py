# -*- coding: utf-8 -*-
# Copyright (c) 2014 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE.TXT file)

from article.models import Category

def add_categories(request):
  return { 'categories': Category.objects.all() }
