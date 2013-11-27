# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Login(models.Model):
    logintime = models.DateTimeField(primary_key=True)
    countrycode = models.CharField(max_length=3, blank=True)
    state = models.CharField(max_length=20, blank=True)
    username = models.ForeignKey('User', db_column='username')
    class Meta:
        db_table = 'Login'

class Messagesent(models.Model):
    author = models.ForeignKey('User', db_column='author', related_name= "author_message_sent")
    receiver = models.ForeignKey('User', db_column='receiver', related_name="receiver_message_sent")
    timesent = models.DateTimeField()
    message = models.CharField(max_length=1000)
    class Meta:
        db_table = 'MessageSent'

class Profile(models.Model):
    id = models.BigIntegerField(primary_key=True)
    backgroundcolor = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = 'Profile'

class User(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    profileid = models.IntegerField()
    isonline = models.ForeignKey(Profile, null=True, db_column='isonline', blank=True)
    class Meta:
        db_table = 'User'

class Userfriends(models.Model):
    userowner = models.ForeignKey(User, db_column='UserOwner', related_name="owner_message_sent") # Field name made lowercase.
    userfriend = models.ForeignKey(User, db_column='UserFriend', related_name="friend_message_sent") # Field name made lowercase.
    class Meta:
        db_table = 'UserFriends'

