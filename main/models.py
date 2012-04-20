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
    def delete(self, *args, **kwargs):
        self.img.delete()
        super(BackgroundImage, self).delete(*args, **kwargs)
        
   
class PictureImage(CommonImage):
    img = models.ImageField(upload_to="pictureimg")
    #tags = models.ManyToManyField(Tag)
    #date = models.DateField()
    def delete(self, *args, **kwargs):
        self.img.delete()
        super(PictureImage, self).delete(*args, **kwargs)