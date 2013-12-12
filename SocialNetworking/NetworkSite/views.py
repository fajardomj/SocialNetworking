from loginhelpers import *
from validationhelpers import *
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http.response import *
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.core import serializers
import json



#home page
def index(request):
    user = get_user_logged_in(request)
    state = getState(user)
    if user is not None:
        return HttpResponseRedirect('/home/')

    return render_to_response('index.html', {'state': state, 'user': user}, context_instance=RequestContext(request))


#profile page
@login_required #if not logged in redirect to /
def profile(request):
    user = ''
    if request.user.is_authenticated():
        user = request.user
    return render_to_response('profile.html', {'user': user}, context_instance=RequestContext(request))

#authenication of user
#@ensure_csrf_cookie
@csrf_exempt
def login_user(request):
    if request.GET and not request.user.is_authenticated():
        return HttpResponseRedirect('/')
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
            return render_to_response('index.html', {'state': state, 'user': user}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')

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
   user=''
   if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if username is None or password is None or email is None:
            return HttpResponse("No username or password or email")
        user = User.objects.create_user(username, email, password)
       # User.objects.raw('update public.auth_user set profile_url="/profile/%s" where username="%s",username')
        #User.objects.filter(username=username).update(profile_url="/profile/"+username)
        ##user.profile_url = '/profile/' + username + '/'
        user.save()
        login_user(request)
   return render_to_response('profile.html', {'user': user}, context_instance=RequestContext(request))


#AJAX checks if username is taken
@csrf_exempt
def check_username(request):
    data = json.loads(request.body)
    username = data.get('username')
    if username is not None:
        data = {"isValid": username_available(username)}
        return HttpResponse(json.dumps(data), content_type="application/json")
    return HttpResponse(json.dumps({"isValid": False}), content_type="application/json")
@csrf_exempt
def check_email(request):
    data = json.loads(request.body)
    email = data.get('email')
    if email is not None:
        data = {"isValid": email_available(email)}
        return HttpResponse(json.dumps(data), content_type="application/json")
    return HttpResponse(json.dumps({"isValid": False}), content_type="application/json")

def get_all_users(request):
    data = serializers.serialize('json', User.objects.all(), fields=('username'))
    #data = {"fields":["username","hi"]}

    return HttpResponse(data, content_type="application/json")


#def getMessage(request,username):
  #  if request.is_ajax() and request.POST:


def message_user(request):
    return HttpResponse('');

#gets profile of user
def get_user_profile(request, username):
    owner = None;
    visitor = None;
    isOwner = False;
    try:
        owner = User.objects.get(username=username)

    except User.DoesNotExist:
        raise Http404

    visitor = get_user_logged_in(request)
    isOwner = False
    if visitor is not None:
     if visitor.username == owner.username:
         isOwner = True


    return render_to_response('userprofile.html', {'visitor': visitor, 'owner': owner, 'isOwner': isOwner}, context_instance=RequestContext(request))