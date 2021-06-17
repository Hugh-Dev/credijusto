from django.http.response import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View
import pandas as pd
import secrets
import requests
import os
from .forms import TokenForm
from .models import TokenModel

# Create your views here.

"""▌ ▌      ▌        ▐  ▌
   ▙▄▌▌ ▌▞▀▌▛▀▖▛▀▖▌ ▌▜▀ ▛▀▖▞▀▖▛▀▖▞▀▖▞▀▖▙▀▖
   ▌ ▌▌ ▌▚▄▌▌ ▌▙▄▘▚▄▌▐ ▖▌ ▌▌ ▌▌ ▌▛▀ ▛▀ ▌
   ▘ ▘▝▀▘▗▄▘▘ ▘▌  ▗▄▘ ▀ ▘ ▘▝▀ ▘ ▘▝▀▘▝▀▘▘  2021"""

"""
Hughpythoneer
@author Hugo Ramírez
@copyright Hughpythoneer
@cto Hughpythoneer
@support hughpythoneer@gmail.com
@phone: +52 998 392 0629
@date 15-06-2021
@version 1.0.0
"""

class IndexView(View):
	"""docstring for IndexView"""
	template_name = 'template.starter.html'
	def get(self, request): 
         return render(request, self.template_name)

class RequestTokenView(View):
	"""docstring for RequestTokenView"""
	template_name = 'template.starter.html'
	def get(self, request): 
         token = secrets.token_hex(20)
         context = {'token':token}
         tokens = TokenModel.objects.create(token=token, status="active", life=5)
         tokens.save()
         return render(request, self.template_name, context)

class ApiRestView(View):
    """docstring for ApiRestView"""
    form_class = TokenForm
    template_name = 'template.starter.html'
    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            token = form.cleaned_data['token']
            queryset = TokenModel.objects.filter(token=token)
            for i in queryset:
                fungible_token = i.token
                life = i.life
            
            if token == fungible_token:
                """Update token life"""
                #update = TokenModel.objects.filter(token=token).update(life=life-1)

                """Api Rest Fixer """
                api = pd.read_json('http://data.fixer.io/api/latest?access_key=8a3b70c7922a9348614d7708f45b3427&symbols=MXN')
                df = pd.DataFrame(api)
                date_fixer_api = df.date
                date_fixer_api = date_fixer_api[0].date().strftime("%d/%m/%y")
                value_fixer_api = df.rates
                value_fixer_api = value_fixer_api.values[0]

                """ Official Journal of the Federation https://www.banxico.org.mx/tipcamb/tipCamMIAction.do """

                df = pd.read_html('https://www.banxico.org.mx/tipcamb/tipCamMIAction.do')
                df_values = df[6].values
                df = pd.DataFrame(data=df_values)
                df = df.dropna()
                df = df.loc[0:2]
                date_banxico_page = df.at[2, 0]
                value_banxico_page = df.at[2, 3]


                """ Api Rest Banxico"""
                token= 'd906a65284a766c522a100057936491f924d7692941d5c5937f7671fb6e7da6e'
                url = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/oportuno?token=%s'% token
                data = requests.get(url)
                dict_j  = data.json()
                for value in dict_j.values():
                    for v in value.values():
                        for k in v:
                            info = k['datos']
                            data = dict(info[0])
                            value_banxico_api = data['dato']
                            date_banxico_api = data['fecha']


                    
                    format = {
                        "rates": {
                            'provider_1':{
                                'last_update':date_fixer_api,
                                'value': value_fixer_api,
                            },
                            'provider_2_variant_1':{
                                'last_update': date_banxico_page,
                                'value': value_banxico_page,
                            },
                            'provider_2_variant_2':{
                                'last_update': date_banxico_api,
                                'value': value_fixer_api,
                            }
                        }
                    }
            
                context = {'table':'Rates:','authtoken':token,'date_fixer_api':date_fixer_api,'value_fixer_api':value_fixer_api,'date_banxico_page':date_banxico_page,'value_banxico_page':value_banxico_page,'date_banxico_api':date_banxico_api,'value_banxico_api':value_banxico_api}
                return render(request, self.template_name, context)
            else:
                context = {'message':'Error in response'}
                return render(request, self.template_name, context)

        context = {'message':'Error in response'}
        return render(request, self.template_name, context)
    

class StatusTokenView(View):
    """docstring for StatusTokenView"""
    form_class = TokenForm
    template_name = 'template.starter.html'
    def get(self, request):
        form = self.form_class()
        context = {'status': form}
        return render(request, self.template_name, context)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            token = form.cleaned_data['token']
            status = TokenModel.objects.filter(token=token)
            context = {'status_table':status}
            return render(request, self.template_name, context)
        context = {'message': 'Error in response'}
        return render(request, self.template_name)


class EnpointView(View):
    """docstring for EnpointView"""
    template_name = 'template.starter.html'
    def get(self, request, token):
        """Update token life"""
        queryset = TokenModel.objects.filter(token=token)
        for i in queryset:
            life = i.life
            update = TokenModel.objects.filter(token=token).update(life=life-1)

        """Api Rest Fixer """
        api = pd.read_json('http://data.fixer.io/api/latest?access_key=8a3b70c7922a9348614d7708f45b3427&symbols=MXN')
        df = pd.DataFrame(api)
        date_fixer_api = df.date
        date_fixer_api = date_fixer_api[0].date().strftime("%d/%m/%y")
        value_fixer_api = df.rates
        value_fixer_api = value_fixer_api.values[0]

        """ Official Journal of the Federation https://www.banxico.org.mx/tipcamb/tipCamMIAction.do """

        df = pd.read_html('https://www.banxico.org.mx/tipcamb/tipCamMIAction.do')
        df_values = df[6].values
        df = pd.DataFrame(data=df_values)
        df = df.dropna()
        df = df.loc[0:2]
        date_banxico_page = df.at[2, 0]
        value_banxico_page = df.at[2, 3]


        """ Api Rest Banxico"""
        token= 'd906a65284a766c522a100057936491f924d7692941d5c5937f7671fb6e7da6e'
        url = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/oportuno?token=%s'% token
        data = requests.get(url)
        dict_j  = data.json()
        for value in dict_j.values():
            for v in value.values():
                for k in v:
                    info = k['datos']
                    data = dict(info[0])
                    value_banxico_api = data['dato']
                    date_banxico_api = data['fecha']


            
            format = {
                "rates": {
                    'provider_1':{
                        'last_update':date_fixer_api,
                        'value': value_fixer_api,
                    },
                    'provider_2_variant_1':{
                        'last_update': date_banxico_page,
                        'value': value_banxico_page,
                    },
                    'provider_2_variant_2':{
                        'last_update': date_banxico_api,
                        'value': value_fixer_api,
                    }
                }
            }
        
            import json
            data = {}
            data['Rates'] = []
            data['Rates'].append({
                'provider': '1',
                'variant': 'None',
                'last_update': date_fixer_api,
                'value': value_fixer_api})
            data['Rates'].append({
                'provider': '2',
                'variant': '1',
                'last_update': date_banxico_page,
                'value': value_banxico_page})
            data['Rates'].append({
                'provider': '2',
                'variant': '2',
                'last_update': date_banxico_api,
                'value': value_fixer_api})
        response = JsonResponse(data)
        content = response.content
        return HttpResponse(content)
