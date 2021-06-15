import secrets
import pandas as pd
import os


# test
"""tk = secrets.token_hex(20)
data = {'token':[tk], 'lifes':[5], 'status': True}
df = pd.DataFrame(data)
tokens = df.to_csv('tokens.csv', index=None)"""
#To csv

pwd = os.getcwd() 
file = 'tokens.csv'
path = '{}/{}'.format(pwd, file)
tk = secrets.token_hex(20)
data = {'token':[tk], 'life':[5], 'status': True}
df = pd.DataFrame(data=data)
df.to_csv(path, mode='a', index=False, header=False)