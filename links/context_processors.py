# -*- coding: utf-8 -*-
# Copyright (c) 2014 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE.TXT file)

from links.models import Link

def add_sidebar_links(request):
  sidebar_links = Link.objects.filter(in_sidebar=True)
  sidebar_links = sidebar_links.order_by('sidebar_ordering')
  return { 'sidebar_links' : sidebar_links }


