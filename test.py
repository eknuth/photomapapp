from photomap.models import *

m = Map()

m.save()

photos = geoPhoto.objects.all()

m.photos = photos

m.save()

m.getKML()

