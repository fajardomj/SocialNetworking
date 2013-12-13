# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

import views

urlpatterns = patterns('',
    # Example chat room.
    url(r"room/(?P<id>\d+)/$", views.window, name="jqchat_test_window"),
    url(r"room/(?P<id>\d+)/ajax/$", views.BasicAjaxHandler, name="jqchat_ajax"),
    url(r"create/", views.createChat, name="create_chat"),
    url(r"get_room/(?P<user>\w+)/(?P<visitor>\w+)", views.getRoom, name="get_room"),
    # Second example room - adds room descriptions.
    url(r"room_with_description/(?P<id>\d+)/$", views.WindowWithDescription, name="jqchat_test_window_with_description"),
    url(r"room_with_description/(?P<id>\d+)/ajax/$", views.WindowWithDescriptionAjaxHandler, name="jqchat_test_window_with_description_ajax"),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



