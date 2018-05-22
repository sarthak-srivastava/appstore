from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CyAppStore.views.home', name='home'),
    # url(r'^CyAppStore/', include('CyAppStore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social_django.urls', namespace='social')),

    url(r'^$',          'apps.views.apps_default', name='default-page'),
    url(r'^apps/',       include('apps.urls')),
    url(r'^search',      include('search.urls')),
    url(r'^download/',   include('download.urls')),
    url(r'^submit_app/', include('submit_app.urls')),
    url(r'^users/',      include('users.urls')),
    url(r'^help/',       include('help.urls')),
    url(r'^backend/',    include('backend.urls')),
)

if settings.DJANGO_STATIC_AND_MEDIA:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
