from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def signup(request):
    template = loader.get_template('signup.html')
    context = {}
    return HttpResponse(template.render(context, request))
