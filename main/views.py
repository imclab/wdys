# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Tag, BackgroundImage, PictureImage
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.views.decorators.csrf import csrf_exempt
from forms import BackgroundImageForm, PictureImageForm
from django.shortcuts import render_to_response
import traceback

def main(request):
    images = PictureImage.objects.all()
    t = loader.get_template('main.html')
    c = RequestContext(request, { 'images': images })
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

@csrf_exempt
def upload_background(request):
    if request.method == "POST":
        index = request.FILES["Filedata"].name.rfind(".");
        image = BackgroundImage(name=request.FILES["Filedata"].name[0:index])
        image.img.save(request.FILES["Filedata"].name, request.FILES["Filedata"])
        return HttpResponse("Upload completed\r\n") 
    else:
        c = RequestContext(request)
        t = loader.get_template("upload_background.html")
        return HttpResponse(t.render(c))

@csrf_exempt
def upload_picture(request):
    if request.method == "POST":
        print("PODST\n")
        index = request.FILES["Filedata"].name.rfind(".");
        image = PictureImage(name=request.FILES["Filedata"].name[0:index])
        image.img.save(request.FILES["Filedata"].name, request.FILES["Filedata"])
        return HttpResponse("Upload completed\r\n") 
    else:
        c = RequestContext(request)
        t = loader.get_template("upload_picture.html")
        return HttpResponse(t.render(c))    
    

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

@csrf_exempt
def delete_picture_image(request, image_id):
    image = PictureImage.objects.get(pk=image_id)
    if image is not None:
        image.delete()
    return HttpResponse("Delete completed\r\n")  

@csrf_exempt
def edit_picture_image(request, image_id):
    if request.method == "POST":
        image = PictureImage.objects.get(pk=image_id)
        form = PictureImageForm(request.POST, instance=image)
        if form.is_valid():
            form.save()
            print("form saved\n")
        else:
            print("not valid\n")
    return HttpResponse("Edit completed\r\n")  

def picture_list(request):
    #render_to_response("background_list.html");
    images = PictureImage.objects.all()
    print(images)
    forms = []
    for image in images:
        #form = BackgroundImageForm(instance=image, initial={'image_id': image.id})
        form = PictureImageForm(instance=image)
        forms.append(form)
    zipped_images = zip(images,forms)    
    c = RequestContext(request, {'pictures':zipped_images})
    t = loader.get_template('picture_list.html')
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