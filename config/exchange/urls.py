# -*- coding: utf-8 -*-
from django.urls import path
from .views import *

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
    #path('request/token', TokenView.as_view(), name='token'),
    path('request/token', RequestTokenView.as_view(), name='request-token'),
    path('status/token', StatusTokenView.as_view(), name='status-token'),
    path('exchange/api', ApiRestView.as_view(), name='api-rest')
]