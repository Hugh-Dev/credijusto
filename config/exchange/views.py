from django.shortcuts import render, redirect
from django.views.generic import View
import pandas as pd
import secrets
import os


# Create your views here.
"""▌ ▌      ▌        ▐  ▌
   ▙▄▌▌ ▌▞▀▌▛▀▖▛▀▖▌ ▌▜▀ ▛▀▖▞▀▖▛▀▖▞▀▖▞▀▖▙▀▖
   ▌ ▌▌ ▌▚▄▌▌ ▌▙▄▘▚▄▌▐ ▖▌ ▌▌ ▌▌ ▌▛▀ ▛▀ ▌
   ▘ ▘▝▀▘▗▄▘▘ ▘▌  ▗▄▘ ▀ ▘ ▘▝▀ ▘ ▘▝▀▘▝▀▘▘  2021"""

class IndexView(View):
	"""docstring for IndexView"""
	template_name = 'template.starter.html'
	def get(self, request): 
         return render(request, self.template_name)

class AddTokenView(View):
	"""docstring for IndexView"""
	template_name = 'template.index.html'
	def get(self, request): 
         token = secrets.token_hex(20)
         context = {'token':token}
         return render(request, self.template_name, context)

class ApiView(View):
	"""docstring for IndexView"""
	template_name = 'template.index.html'
	def get(self, request): 
         return render(request, self.template_name)


class TokenView(View):
    """docstring for IndexView"""
    template_name = 'template.tokens.html'
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        pwd = os.getcwd()
        file = 'tokens.csv'
        path = '{}/{}'.format(pwd, file)
        df = pd.read_csv(path, index_col=None)
        
        #status_change = df.loc[(df['token'] == columns[0]), "status"] = "False"
        #status_change = df.loc[columns[0]]
        #token = df.loc[0]
        #print(token[0])
        token = df.at[0, 'token']
        #lifes = df.at[0, 'lifes']
        #df.at[0, 'lifes'] = lifes - 1
        
        context = {'token':token}
        #status_change = df.loc[(status == True), status] = False
        df.at[0, 'status'] = False
        status = df.at[0, 'status']
        print(df)
        df.to_csv(path, mode='w', index=False, header=True)
        context = {'token': token}
        return render(request, self.template_name, context)

class CreateTokensView(View):
    template_name = 'template.index.html'
    def get(self, request):
        pwd = os.getcwd() 
        file = 'tokens.csv'
        path = '{}/{}'.format(pwd, file)
        if path:
            tk = secrets.token_hex(20)
            data = {'token':[tk], 'life':[5], 'status':True}
            df = pd.DataFrame(data=data)
            df.to_csv(path, mode='a', index=False, header=False)
        else:
            print('...............')
            tk = secrets.token_hex(20)
            data = {'token':[tk], 'lifes':[5], 'status': True}
            df = pd.DataFrame(data)
            df.to_csv('tokens.csv', index=None)
        return redirect('/')


"""df = pd.read_csv(path, index_col=None)
columns = df.columns
columns_dict = {}
count = 0
for name in columns:
    count += 1
    columns_dict['column{}'.format(count)] = name"""

