from django.contrib.auth.models import User

class WebAuth(object):

# Create an authentication method
# This is called by the standard Django login procedure
    def authenticate(self, username=None, password=None):

        try:
            if username is not None:
        # Try to find a user matching your username

                user = User.objects.get(self, pk=username)
                if user.password != password:
                    return None
        except User.DoesNotExist:
        # No user was found, return None - triggers default login failed
            return None

        return None

            # Required for your backend to work properly - unchanged in most scenarios

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None



