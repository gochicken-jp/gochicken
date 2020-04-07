# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:42:14 2020

@author: gochicken
"""

import pandas as pd 
df = pd.read_csv('input.txt')
df = df.iloc[:52]
df['number'] = df.iloc[:,0].str.split(':').str[0]
df['string'] = df.iloc[:,0].str.split(':').str[1]
df = df.set_index('string')['number'].astype(int).to_frame()
d = df.to_dict()
d = d['number']
D={}
m=895935051710483657676643043460
for s,i in d.items():
    if m % i == 0:
        D[s] = i
        
print(sorted(D,key=D.get))
