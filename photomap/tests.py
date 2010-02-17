"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

class ModelTest(TestCase):
    def img_save(self):
        """
        Tests that we can save a Photo.
        """
#        self.failUnlessEqual(1 + 1, 2)
        from PIL import Image
        from models import Photo
        
        im = Image.open('P1020515.JPG')
        photo = Photo()
        
        photo.img=im
        photo.url='http://go00gle.com'
        photo.save()
        self.failUnlessEqual(im,photo.img)
        self.failUnlessEqual(photo.url, 'http://google.com')

def runTest():  
    m = ModelTest()
    m.img_save()
