from django.test import TestCase
from .models import Image,Album,tags
# Create your tests here.
class ImageTestClass(TestCase):

    #set up method
    def setUp(self):
        self.photo_image= Image(image_name ='camera',description ='family')

    #Testing instance 
    def test_instance(self):
        self.assertTrue(isinstance(self.photo_image,Image))

    #Testing save method
    def test_save_method(self):
        self.photo_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    #Testing delete method
    # def test_delete_method(self):
    #     self.photo_image.delete_image()
    #     images = Image.objects.all()
    #     self.assertEqual(len(Image.images),1)

class AlbumTestClass(TestCase):

    def setUp(self):
        #Creating a new image and saving it
        self.photo_image= Image(image_name = '')