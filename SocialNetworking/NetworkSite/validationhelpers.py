from django.contrib.auth.models import User
#checks if user is present
def username_available(username):
    if User.objects.filter(username=username).count():
        return False
    return True

def email_available(email):
    if User.objects.filter(email=email).count():
        return False
    return True
def profile_available(username):
    if User.objects.filter(username=username).count():
        return False
    return True