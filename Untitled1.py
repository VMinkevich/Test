#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


get_ipython().run_line_magic('matplotlib', 'inline')

sns.set(style="darkgrid")


# In[3]:


train = pd.read_csv("train.csv")
example = pd.read_excel('example.xlsx', engine='openpyxl')
counterparitys = pd.read_csv("Контрагенты по годам.csv")
buys = pd.read_csv("Покупка с ОРЭ 2019-2020.csv")
tariffs = pd.read_csv("Тарифы 2019-2020.csv")


# In[11]:


buys


# In[114]:


a = pd.DataFrame(counterparitys.isnull().sum())
a_nan = a[a[0] != 0]

#Есть пропуски в дата докум.3 и Дата постановки на оплату (оконч. платеж.)
a_nan_over_10 = a_nan[a_nan[0] > 10]

#Удаляем Дата постановки на оплату (оконч. платеж.), оч много пропусков
counterparitys_1 = counterparitys.drop(columns='Дата постановки на оплату (оконч. платеж.)')
counterparitys_1


# In[120]:


# дропнули дубли
counterparitys_1 = counterparitys_1.drop_duplicates(subset=['% оплаты', 'сумма оплачено,без НДС', 'Контрагент'], keep='last')
counterparitys_1


# In[75]:


counterparitys['Контрагент'].unique()


# In[58]:


train.describe()[['Сумма в RUB']]


# In[27]:


m = Prophet()
m.fit(train_pr)


# In[31]:


future = m.make_future_dataframe(periods=365)
future.tail()


# In[32]:


forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()


# In[33]:


fig1 = m.plot(forecast)


# In[34]:


fig2 = m.plot_components(forecast)


# In[132]:


l = [2,4,1,2,4,2,4,36,7]

for k in range(0,len(l)-1):
    if l[k] > l[k+1]:
        l[k+1], l[k] = l[k], l[k+1]
print(l)


# In[73]:


def ins_sort(A):
    for i in range(1,len(A)):
        for j in range(i-1, -1, -1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            else:
                break
                

def ins_sort_while(A):
    for i in range(1, len(A)):
        j = i - 1
        while A[j] > A[j+1] and j >= 0:
            A[j], A[j+1] = A[j+1], A[j]
            j -= 1


# In[75]:


B = [2,4,34,3,2,0]
ins_sort_while(B)
B


# In[ ]:




