from django.contrib.auth import authenticate
from django.shortcuts import render_to_response
from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie

def index(request):
    state ="Pre Login"
    return render_to_response('index.html', {'state': state})

def login(user):
    return render_to_response('profile.html', {'name': user.username})

def login_user(request):

    state = "login"
    username = ''
    password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.isonline:
                state = "Logged in"
                login(user)
            else:
                state = "error"
        else:
            state = "user is none"

    return render_to_response('index.html', {'state': state, 'username': username})
