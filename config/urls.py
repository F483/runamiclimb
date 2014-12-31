from django.conf.urls import patterns, include, url
from django.conf.urls.static import static 
from django.contrib import admin
import settings

urlpatterns = patterns('',
  url(r'^admin/', include(admin.site.urls)),
  url(r'^captcha/', include('captcha.urls')),
  url(r'^photologue/', include('photologue.urls', namespace='photologue')),
  url(r'^paypal/', include('paypal.standard.ipn.urls')),
  url(r'^support/', include('support.urls')),
  url(r'^comment/', include('comment.urls')),
  url(r'^page/', include('page.urls')),
  url(r'^', include("article.urls")),
)

if settings.DEBUG:                                                                                              
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

