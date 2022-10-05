from django.http import HttpResponse
from django.template import loader
from .models import Film, Director


def index(request):
    template = loader.get_template('index.html')
    context = {'films': Film.objects.all()}
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def signup(request):
    template = loader.get_template('signup.html')
    context = {}
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        print(username, email, password, password2, request.method)
    return HttpResponse(template.render(context, request))

def directors(request):
    template = loader.get_template('directors.html')
    context = {'directors': Director.objects.all()}
    return HttpResponse(template.render(context, request))
