# -*- coding: utf-8 -*-
# Copyright (c) 2014 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE.TXT file)

from django.conf import settings as _settings
from photologue.models import Gallery, PhotoSize

def add_settings(request):
  return { 'settings': _settings }

def add_titlebar_photos(request):
  galleries = Gallery.objects.filter(title="Titlebar photos")
  sizes = PhotoSize.objects.filter(name="titlebar_photo")
  if galleries and sizes:
    return { 
        'titlebar_photos' : galleries[0].photos.all()[:5],
        'titlebar_photo_size' : sizes[0]
    }
  return { 'titlebar_photos' : [], 'titlebar_photo_size' : None }
