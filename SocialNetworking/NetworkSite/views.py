from loginhelpers import *
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http.response import *
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.core import serializers
from django.forms.models import model_to_dict
import json



#home page
def index(request):
    user = get_user_logged_in(request)
    state = getState(user)
    if user is not None:
        return render_to_response('profile.html', {'username': user.username}, context_instance=RequestContext(request))

    return render_to_response('index.html', {'state': state, 'user': user}, context_instance=RequestContext(request))


#profile page
@login_required #if not logged in redirect to /
def profile(request):
    user = ''
    if request.user.is_authenticated():
        user = request.user
    return render_to_response('profile.html', {'user': user}, context_instance=RequestContext(request))

#authenication of user
@ensure_csrf_cookie
def login_user(request):
    user=''
    state = ''
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['logged_in_user'] = user.id
                state = "You're successfully logged in!"
                return render_to_response('profile.html', {'state':state,'user':user}, context_instance=RequestContext(request))
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    else:
        user = get_user_logged_in(request)
        state = getState(user)
    return render_to_response('index.html', {'state': state, 'user': user}, context_instance=RequestContext(request))

#logs out user
def logout(request):
    if request.method == 'POST':
        try:
            del request.session['logged_in_user']
        except KeyError:
            pass
    user = get_user_logged_in(request)
    state = getState(user)

    return render_to_response('index.html', {'state': state, 'user': user}, context_instance=RequestContext(request))

#serves sign up page
def signup(request):
    user = get_user_logged_in(request)
    return render_to_response('signup.html', {'user': user}, context_instance=RequestContext(request))

#creates user
def create(request):
    user =''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if username is None or password is None or email is None:
            return HttpResponse("No username or password or email")
        user = User.objects.create_user(username, email, password)
        user.save()
        login_user(request)
    return render_to_response('profile.html', {'user': user}, context_instance=RequestContext(request))


#AJAX checks if username is taken
@csrf_exempt
def check_username(request):
    data = json.loads(request.body)
    username = data.get('username')
    if username is not None:
        return username_present(username)
    return HttpResponse(False)

def get_all_users(request):
   ## data = serializers.serialize('json', User.objects.all(), fields=('username'))
    data = {"username" :"matt"},{"username": "blah"}
    return HttpResponse(data, content_type="application/json")

    #return HttpResponseRedirect('/')

#serves error page
def error(request):
    return render_to_response('error.html')

#def get_another_profile(request):
    #get another users profile and return it
    # return render_to_response('profile.html', {'user': user}, context_instance=RequestContext(request))