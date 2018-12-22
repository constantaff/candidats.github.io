from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from election.models import Elect


def index(request):
    return render(request=request, template_name="index.html")


def votes(request):
    if request.user.is_authenticated:
        all_elect = Elect.objects.all()
        context = {
            'levinkov': all_elect.get(pk=1),
            'radchenko': all_elect.get(pk=2),
            'gorbunov': all_elect.get(pk=3)
        }
        return render(request=request, template_name="votes.html", context=context)
    else:
        return login_page(request)


def login_page(request):
    context = {
        'is_auth': request.user.is_authenticated
    }
    return render(request=request, template_name='login.html', context=context)


def try_login(request):
    if request.user.is_authenticated:
        logout(request)
        return login_page(request)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/votes/')
    else:
        return login_page(request)


def try_register(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(username, 'lennon@thebeatles.com', password)
    user.save()
    if user is not None:
        login(request, user)
        return redirect('/votes/')
    else:
        return login_page(request)


def add_vote(request, elect_id):
    if request.user.profile.has_voted:
        return index(request)
    elect = Elect.objects.get(pk=elect_id)
    elect.votes += 1
    elect.save()
    user = User.objects.get(username=request.user.username)
    user.profile.has_voted = True
    user.save()
    return votes(request)


def elements(request):
    return render(request=request, template_name="elements.html")

def donate(request):
    return render(request=request, template_name="donate.html")
