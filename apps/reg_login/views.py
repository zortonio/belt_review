from django.shortcuts import render, HttpResponse, redirect
from .models import User

# Create your views here.
def index(req):
    return render(req, 'reg_login/index.html')

def validate(req, route):
    if route=='register':
        if User.objects.register(req):
            return redirect('books:index')
        else:
            return redirect('reg_login:index')
    elif route=='login':
        if User.objects.login(req):
            return redirect('books:index')
        else:
            return redirect('reg_login:index')

def user(req, id):
    context = {
        'user': User.objects.get(id=id),
    }
    return render(req, 'reg_login/user.html', context)
