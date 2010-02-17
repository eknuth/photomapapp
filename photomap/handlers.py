import re

from piston.handler import BaseHandler
from piston.utils import rc, throttle

from photomap.models import geoPhoto, Map

class PhotoHandler(BaseHandler):
    fields = ('id', 'image', 'placemark', 'coords')
    allowed_methods = ('GET','PUT', 'DELETE', 'POST' )

    model = geoPhoto
    
    def create(self,request):       
    
        p = geoPhoto()
        p.create(request.FILES['Filedata'])
        p.save()       
        print "saved"
        return rc.ALL_OK
 
            
class MapHandler(BaseHandler):
    allowed_methods = ('GET','PUT', 'DELETE', 'POST')
    fields = ('id', 'owner', 'name')
    
    model = Map

