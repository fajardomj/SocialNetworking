from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SocialNetworking.views.home', name='home'),
    # url(r'^SocialNetworking/', include('SocialNetworking.foo.urls')),
    url(r'^$', 'NetworkSite.views.index',name='login'),
    url(r'^home/', 'NetworkSite.views.profile',name='home'),
    url(r'^login/', 'NetworkSite.views.login_user', name='login_user'),
    url(r'^logout/', 'NetworkSite.views.logout', name='logout'),
    url(r'^signup/', 'NetworkSite.views.signup', name='signup'),
    url(r'^check_username/', 'NetworkSite.views.check_username', name='check_username'),
    url(r'^check_email/', 'NetworkSite.views.check_email', name='check_email'),
    url(r'^create/', 'NetworkSite.views.create', name='create'),
    url(r'^get_users/', 'NetworkSite.views.get_all_users', name='get_users'),
    url(r'^profile/(?P<username>\w+)/$', 'NetworkSite.views.get_user_profile', name='user_profile'),
    url(r'^message/(?P<username>\w+)/$', 'NetworkSite.views.message_user', name='message'),



    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

# ... the rest of your URLconf goes here ...
   # url(r'^api-auth/', include('djangorestframework.urls', namespace='rest_framework'))

    #url(r'^admin/', include(admin.site.urls)),
)
