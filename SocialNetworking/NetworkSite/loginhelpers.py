from django.contrib.auth.models import User

#checks if user is present
def username_present(username):
    if User.objects.filter(username=username).count():
        return True

    return False

#gets the current user that is logged in
def get_user_logged_in(request):
    id = request.session.get('logged_in_user')
    user =''
    if id is not None:
        user = User.objects.get(pk=id)
        return user
    return None

#gets the State of a user
def getState(user):
    if user is not None:
        return "You are logged in!"
    else:
        return "Please Login!"

