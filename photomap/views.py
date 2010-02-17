# Create your views here.
from photomap.models import geoPhoto
from django.http import HttpResponse
from django.shortcuts import render_to_response



from django import http
from django import forms
from django.shortcuts import render_to_response



def maps(request):
    return render_to_response('maps.html')

def kml(request):
	photos = geoPhoto.objects.order_by('-id')
	return render_to_response('base.kml', {'photos': photos},
									mimetype="application/vnd.google-earth.kml+xml")

def photos(request):
    photos = geoPhoto.objects.order_by('-id')
    return render_to_response('photos2.html', {'photos': photos})
        
    
def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))