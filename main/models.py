from django.db import models
    
class Tag(models.Model):
    name = models.URLField(max_length=30)
    
#class City(models.Model):
#    name = models.URLField(max_length=30)

class CommonImage(models.Model):
    name = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    class Meta:
        abstract = True
    
class BackgroundImage(CommonImage):
    img = models.ImageField(upload_to="backgroundimg")
    description = models.TextField(blank=True)
   
class PictureImage(CommonImage):
    img = models.ImageField(upload_to="pictureimg")
    #tags = models.ManyToManyField(Tag)
    #date = models.DateField()