# -*- coding: utf-8 -*-
from django.urls import path
from .views import *

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
    path('request/token', RequestTokenView.as_view(), name='request-token'),
    path('status/token', StatusTokenView.as_view(), name='status-token'),
    path('exchange/api', ApiRestView.as_view(), name='api-rest'),
    path('api/authtoken/token=<str:token>&base=USD&change=MXN', EnpointView.as_view(), name='enpoint-rest-api')
]