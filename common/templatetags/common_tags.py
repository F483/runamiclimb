# -*- coding: utf-8 -*-
# Copyright (c) 2014 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE.TXT file)

import bleach
import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def render_markdown(usertext):
  tags = [
    'a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'br',  'h1', 'h2', 'h3',
    'h4', 'h5', 'h6', 'hr', 'i', 'img', 'li', 'ol', 'p', 'pre', 'strong', 'ul'
  ]
  attributes = {
    'a': ['href', 'title'],
    'abbr': ['title'],
    'acronym': ['title'],
    'img' : ['src', 'alt', 'title']
  }
  html = markdown.markdown(usertext) # docs say use bleach instead of safe_mode
  return mark_safe(bleach.clean(html, tags=tags, attributes=attributes))

