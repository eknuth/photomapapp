from django.conf.urls.defaults import *
from photomap import views
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from django.contrib.auth.views import login, logout


#import handlers 
from photomap.handlers import MapHandler, PhotoHandler

#set up authentication
#auth = HttpBasicAuthentication(realm="photomapapp")
#ad = { 'authentication': auth }

#set up resources
#map_resource = Resource(handler=MapHandler, **ad)
#photo_resource = Resource(handler=PhotoHandler, **ad)
map_resource = Resource(handler=MapHandler)
photo_resource = Resource(handler=PhotoHandler)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
				   (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/eknuth/photomapapp/media/'}),
				   (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/eknuth/photomapapp/static/'}),

				   (r'^admin/', include(admin.site.urls)),
				   
				   url(r'^photos$', views.photos),
				   url(r'^maps$', views.maps),
				   url(r'^maps.kml$', views.kml),
				
				   
				   url(r'^api/photo/(?P<id>[^/]+)$', photo_resource), 
				   url(r'^api/photos$', photo_resource),
				   url(r'^api/map/(?P<id>[^/]+)$', map_resource), 
				   url(r'^api/maps$', map_resource),
    				   (r'^accounts/login/$',  login),
    				   (r'^accounts/logout/$', logout),


    # Example:
    # (r'^photomapapp/', include('photomapapp.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
