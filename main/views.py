# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Tag, CommonImage
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

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
    t = loader.get_template("upload.html")
    c = RequestContext(request)
    return HttpResponse(t.render(c))

@csrf_exempt
def uploadImages(request):
    print(request.COOKIES)
    print("shit0\n")
    if request.method == "POST":
        print("shit1\n")
#        sid = request.POST['sessionid']
#        print(sid)
#        session = request.session
#        session._set_session_key(sid)
#        session._get_session()
        image = CommonImage()
        print("shit2\n")
        image.img.save(
            request.FILES['Filedata'].name,
            request.FILES['Filedata'],
            save=True
        )
        print("shit3\n")
    
    print("shit\n")
    
    response = HttpResponse()
    response.write("hola\r\n")
    return response
    
def step2(request):
    if request.method == "POST":
        return HttpResponse("asdf")
    else:    
        images = CommonImage.objects.all()
        
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