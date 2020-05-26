from django.db import models

# Create your models here.
class Image(models.Model):
    photo_image = models.ImageField(upload_to = 'photo/')
    image_name = models.CharField(max_length =100)
    description = models.CharField(max_length=100)
    # location_foreign_key
    # category_foreign_key

    def __str__(self):
        return self.photo_image

    def save_image(self):
        self.save()

    # def delete_image(self):
    #     self.delete()

    class Meta:
        ordering = ['photo_image']

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name    

class Album(models.Model):
    travel_image = models.ImageField(upload_to = 'travel/')
    family_image = models.ImageField(upload_to = 'family/')
    old_image = models.ImageField(upload_to = 'old/')
    download_image = models.ImageField(upload_to = 'download/')
    screenshot_image = models.ImageField(upload_to = 'screenshot/')
    image = models.ForeignKey(Image)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)