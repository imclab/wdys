from django.db import models
    
class Tag(models.Model):
    name = models.URLField(max_length=30)
    
class City(models.Model):
    name = models.URLField(max_length=30)

class CommonImage(models.Model):
    #city = models.ForeignKey(City)
    class Meta:
        abstract = True
    
class BackgroundImage(models.Model):
    img = models.ImageField(upload_to="backgroundimg")
    name = models.CharField(max_length=30, blank=True)
   
class PhotoImage(CommonImage):
    img = models.ImageField(upload_to="photoimg")
    name = models.CharField(max_length=30)
    tags = models.ManyToManyField(Tag)
    date = models.DateField()