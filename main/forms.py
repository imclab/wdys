from django import forms
from django.forms import ModelForm
from models import BackgroundImage

class BackgroundImageForm(ModelForm):
    image_id = forms.IntegerField(widget=forms.HiddenInput)
    class Meta:
        model = BackgroundImage
        exclude = ('img')  


#from wdys.main.models import CityImage
#    
#class CityImageForm(ModelForm):
#    city = forms.ModelChoiceField()
#        
#class SceneImageForm(ModelForm):
#    class Meta:
#        model = SceneImage        
#    
#class SceneImage(CityImage):
#    name = models.CharField(max_length=30)
#    tags = models.ManyToManyField(Tag)
#    date = models.DateField()