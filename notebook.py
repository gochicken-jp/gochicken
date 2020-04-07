# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Data.csv')
X=dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values



#split dataset
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state=0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

dataset.iloc[:,1]
dataset.
dataset.loc()

#get dataframe information
dt.info()
#rename
dataset.rename(column={'':''},inplace=True)
#convert str to float
dataset[''].str.replace('"','').astype(float)
#extract from string
dataset[].str.split().str[]
#drop line or col
dataset.dropna(axis=)
#exporting Dataframe
dataset.to_csv('New name')
#replace missing data
series.fillna('')
#identify & drop duplicated row
df.duplicated()#boolean
df.drop_duplicates()
#frequency table
series.describe()


#read txt file
pd.read_csv('file.txt',parse_dates=['col_name'])

#read csv as list
import csv
opend_file = open('')
read_file = csv.reader(opend_file)
data = list(read_file)

#aggregate 1
dataset.groupby('').agg()

#aggregate 2
dataset.pivot_table(values=,index=,aggfumc=)

#concatenate dataframe
pd.concat([df1,df2],join='join_type')

#merge 
pd.merge([left], [right], how=[str], on=[str])

#differences
df.applymap(function)#element-wise
df.apply(function)# column-wise

#RE
pattern=
r'[Nn]ation'
r'[0-9]'
r'([1-2][0-9][0-9][0-9])'#match year
r'([1-2][0-9]{3})' # same as above
r'(?P<group_name>[1-2][0-9]{3})'give capturing group name

import re
re.search(pattern)

series.str.contains(pattern) #used as filter boolean
series.str.extractall(pattern) 
series.str.replace(pattern,"new string")

#seaborn
import seaborn as sns
sns.heatmap()

#working with json file
import json
f=open('.json')
json.load(f)
json.loads('')#string to Python objects
json.dumps('')#Python objects to string


#connect SQL server 1
import psycopg2
conn = psycopg2.connect("dbname= ,user= ")
cur = conn.cursor()
cur.execute("")
conn.close()

#connect SQL server 2
import sqlite3
conn = sqlite3.connect('job.db')
cur =conn.cursor()
cur.execute("")
result = cur.fetchall/fetchone/fetchmany()
conn.close

fig = plt.figure()
ax1 = fig.subplots()
ax2 = fig.subplots()
ax1.

#余数问题
for a in range('a-zzzz'):
    dictionary[a] += 1
for fizzbuzz in range(100):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)


#是否轴对称
def is_palindrome(dna):
    n_d=len(dna)
    for i in range(n_d // 2):
        if dna[i] != dna[n_d-i-1]:
            return False
    return True

#两列DF转DICT问题
df = pd.read_csv('dataset')
df = df.set_index(['1st column name'])
name_to_email=df.to_dict()['2nd column name']

