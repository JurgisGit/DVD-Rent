from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from .models import Film, Director, Rating
from django.contrib.auth.forms import User
from django.contrib.auth import logout, authenticate, login


def index(request):
    template = loader.get_template('index.html')
    context = {'films': Film.objects.all()}
    return HttpResponse(template.render(context, request))


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')

    template = loader.get_template('login.html')
    context = {}
    return HttpResponse(template.render(context, request))


def signup(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        print(username, email, password, password2, request.method)
        User.objects.create_user(username, email, password)
        return redirect('index')
    elif request.method == "GET":
        template = loader.get_template('signup.html')
        context = {}
        return HttpResponse(template.render(context, request))


def directors(request):
    template = loader.get_template('directors.html')
    context = {'directors': Director.objects.all()}
    return HttpResponse(template.render(context, request))


def logout_user(request):
    logout(request)
    return redirect('index')


def ratings(request):
    template = loader.get_template('ratings.html')
    context = {'ratings': Rating.objects.all()}
    return HttpResponse(template.render(context, request))