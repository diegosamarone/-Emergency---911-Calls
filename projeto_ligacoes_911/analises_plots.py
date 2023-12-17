# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:57:48 2023

@author: Diego
"""

from leitura_dados import pd, sns, df, plt

#criar um countplot de chamadas 911 baseado no Dataframe de tipos: EMS, "Fire " e "Traffic
sns.countplot(x='Reason', data = df)

#informações de tempo
#convertendo a locuna 'timeStamp' em obeto DateTime
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

#Com base na coluna timeStamp use .apply () para criar 3 novas colunas chamadas Hour, Month e Day of Week
df['Hour'] = df['timeStamp'].apply(lambda x: x.hour)
df['Month'] = df['timeStamp'].apply(lambda x: x.month)
df['Day of Week'] = df['timeStamp'].apply(lambda x: x.dayofweek)

#Use o .map () com este dicionário para mapear os nomes das sequências reais para o dia da semana
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)
df['Day of Week']


#countplot da coluna "Day of Week"
sns.countplot(x='Day of Week', data=df, hue='Reason', palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # Ajuste a posição da legenda conforme necessário


