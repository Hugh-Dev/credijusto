# -*- coding: utf-8 -*-
from django.urls import path
from .views import *

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
    path('token', TokenView.as_view(), name='token'),
    path('solicitar/token', AddTokenView.as_view(), name='solicitar-token'),
    path('generate/token', CreateTokensView.as_view(), name='generate-token'),
    path('exchange/api', ApiView.as_view(), name='api')
]