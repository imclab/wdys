# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Tag, BackgroundImage
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.views.decorators.csrf import csrf_exempt
from forms import BackgroundImageForm
from django.shortcuts import render_to_response
import traceback

def main(request):
    t = loader.get_template('main.html')
    indexes = range(1,13)
    c = RequestContext(request, { 'indexes': indexes })
    return HttpResponse(t.render(c))

def make(request):
    t = loader.get_template('make.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))
    
def comment(request):
    try:
        tag = Tag.objects.all()
        print(tag)
    except ObjectDoesNotExist:
        print "Either the entry or blog doesn't exist."
    t = loader.get_template('comment.html')
#   c = RequestContext(request, {"tag":tag})
    c = RequestContext(request)
    return HttpResponse(t.render(c))

def upload(request):
    
    c = RequestContext(request)
    
        
    t = loader.get_template("upload.html")
    return HttpResponse(t.render(c))

@csrf_exempt
def upload_images(request):
    if request.method == "POST":
       
        files = request.FILES
        print(files)
        
        image = BackgroundImage(name=request.FILES["Filedata"].name)
        image.img.save(request.FILES["Filedata"].name, request.FILES["Filedata"])
    
    return HttpResponse("Upload completed\r\n")

@csrf_exempt
def delete_background_image(request, image_id):
    image = BackgroundImage.objects.get(pk=image_id)
    if image is not None:
        image.delete()
    return HttpResponse("Delete completed\r\n")  

@csrf_exempt
def edit_background_image(request, image_id):
    if request.method == "POST":
        image = BackgroundImage.objects.get(pk=image_id)
        form = BackgroundImageForm(request.POST, instance=image)
        if form.is_valid():
            form.save()
            print("form saved\n")
        else:
            print("not valid\n")
    return HttpResponse("Edit completed\r\n")       


def background_list(request):
    #render_to_response("background_list.html");
    images = BackgroundImage.objects.all()
    forms = []
    for image in images:
        #form = BackgroundImageForm(instance=image, initial={'image_id': image.id})
        form = BackgroundImageForm(instance=image)
        forms.append(form)
    zipped_images = zip(images,forms)    
    c = RequestContext(request, {'backgrounds':zipped_images})
    t = loader.get_template('background_list.html')
    return HttpResponse(t.render(c))
    
def step2(request):
    if request.method == "POST":
        return HttpResponse("asdf")
    else:    
        images = BackgroundImage.objects.all()
        
        if images.exists():
            for image in images:
                print(str(image.img)+"\n")
        else:
            images = "asdf"
        t = loader.get_template('step2.html')
        c = RequestContext(request, {'images':images})
        return HttpResponse(t.render(c))
    
def step3(request):
    t = loader.get_template('step3.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))
    
def publish(request):
    t = loader.get_template('publish.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))