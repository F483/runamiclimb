# -*- coding: utf-8 -*-
# Copyright (c) 2014 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE.TXT file)

from page.models import Page

def add_sidebar_pages(request):
  sidebar_pages = Page.objects.filter(in_sidebar=True)
  return { 'sidebar_pages' : sidebar_pages }


