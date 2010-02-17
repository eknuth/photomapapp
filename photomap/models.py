from django.db import models
from PIL import Image
import EXIF


from photologue.models import ImageModel

def DmsToDecimal(degree_num, degree_den, minute_num, minute_den,
                 second_num, second_den):
  """Converts the Degree/Minute/Second formatted GPS data to decimal degrees.

  Args:
    degree_num: The numerator of the degree object.
    degree_den: The denominator of the degree object.
    minute_num: The numerator of the minute object.
    minute_den: The denominator of the minute object.
    second_num: The numerator of the second object.
    second_den: The denominator of the second object.

  Returns:
    A deciminal degree.
  """

  degree = float(degree_num)/float(degree_den)
  minute = float(minute_num)/float(minute_den)/60
  second = float(second_num)/float(second_den)/3600
  return degree + minute + second


def GetGps(data):
  """Parses out the GPS coordinates from the file.

  Args:
    data: A dict object representing the Exif headers of the photo.

  Returns:
    A tuple representing the latitude, longitude, and altitude of the photo.
  """

  lat_dms = data['GPS GPSLatitude'].values
  long_dms = data['GPS GPSLongitude'].values
  latitude = DmsToDecimal(lat_dms[0].num, lat_dms[0].den,
                          lat_dms[1].num, lat_dms[1].den,
                          lat_dms[2].num, lat_dms[2].den)
  longitude = DmsToDecimal(long_dms[0].num, long_dms[0].den,
                           long_dms[1].num, long_dms[1].den,
                           long_dms[2].num, long_dms[2].den)
  if data['GPS GPSLatitudeRef'].printable == 'S': latitude *= -1
  if data['GPS GPSLongitudeRef'].printable == 'W': longitude *= -1
  altitude = None

  try:
    alt = data['GPS GPSAltitude'].values[0]
    altitude = alt.num/alt.den
    if data['GPS GPSAltitudeRef'] == 1: altitude *= -1

  except KeyError:
    altitude = 0

  return latitude, longitude, altitude



    
class geoPhoto(ImageModel):
    """
    A single photo
    
    >>> p = geoPhoto(url='http://google.com', img='')
    >>> i = Image.open('P1020515.JPG')
    >>> p.img = i.thumbnail
    >>> p.img == i.thumbnail
    True
    >>> p.url
    'http://google.com'
    >>> p.save()
    """


    coords = models.CharField(max_length='100')
    
    

    def upload_to(self):
        return 'media/%Y/%m/%d'
        
    def create(self,contents):

        #extract exif and calculate readable coords from complicated exif
        e=EXIF.process_file(contents)
        try:
            (lat,lon,alt) = GetGps(e)
        except:
            print "couldn't do it?"
        
        #save it!
        self.coords = ('%s, %s' % (lon,lat))
        self.image = contents
        self.save()
        
    def placemark(self):
        return """
         <Placemark>
    <name>photomap</name>
    <description>Attached to the ground. Intelligently places itself 
       at the height of the underlying terrain.</description>
    <Point>
      <coordinates>%s,0</coordinates>
    </Point>
  </Placemark>""" % self.coords

  
    def __unicode__(self):
        return self.coords
    
        

class Map(models.Model):
    name = models.CharField(max_length=30)
    owner = models.CharField(max_length=50)
    photos = models.ManyToManyField(geoPhoto)
    
    def __get_kml(self):
        return "test"
    kml = property(__get_kml)
        

    def __unicode__(self):
        return self.name
 
      