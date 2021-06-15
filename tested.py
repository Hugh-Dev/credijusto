import pandas as pd
import numpy as np
import requests

#https://fixer.io/documentation
print('Api Fixer')
api = pd.read_json('http://data.fixer.io/api/latest?access_key=8a3b70c7922a9348614d7708f45b3427&symbols=MXN')
df = pd.DataFrame(api)
fecha = df.date
valor = df.rates

format = {
    'last update': fecha[0].date().strftime("%d/%m/%y"),
    'valor': valor[0],
         }
print(format)



print('-'*20)

"""https://www.banxico.org.mx/tipcamb/tipCamMIAction.do"""
#Banco de México.
print('Noticias Banco de México')
df = pd.read_html('https://www.banxico.org.mx/tipcamb/tipCamMIAction.do')
df_values = df[6].values
df = pd.DataFrame(data=df_values)
df = df.dropna()
df = df.loc[0:2]
fecha = df.at[2, 0]
valor = df.at[2, 3]

format = {
    'last update': fecha,
    'valor': valor
         }
print(format)

print('-'*20)

#'Exchange, {} {}'.format(fecha, valor)
print('Banxico API Rest')
token= 'd906a65284a766c522a100057936491f924d7692941d5c5937f7671fb6e7da6e'
url = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/oportuno?token=%s'% token
data = requests.get(url)
dict_j  = data.json()
for value in dict_j.values():
  for v in value.values():
      for k in v:
          info = k['datos']
          datos = dict(info[0])
          valor = datos['dato']
          fecha = datos['fecha']

format = {
    'last update': fecha,
    'valor': valor
         }
print(format)