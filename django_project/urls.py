from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^', include('head.urls')),
    url(r'^outdoor/', include('outdoor.urls')),
    url(r'^womens/', include('womens.urls')),
    url(r'^mens/', include('mens.urls')),
    url(r'^access/', include('access.urls')),
    url(r'^pet/', include('pet.urls')),
    url(r'^special/', include('special.urls')),
    url(r'^contact/', include('django_contactme.urls')),
    
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




