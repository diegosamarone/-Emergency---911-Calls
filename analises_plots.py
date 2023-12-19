# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:57:48 2023

@author: Diego
"""

'''
Instruções para o usuário:
Execute o código em ordem, começando pelo Bloco 00, 
seguido pelo Bloco 01, Bloco 02, etc.

*sugestão para executar bloco por bloc: shift + enter.

'''

# %% Bloco 00:
from leitura_dados import pd, sns, df, plt

# %% %% Bloco 01: criar um countplot de chamadas 911 baseado no Dataframe de tipos: EMS, "Fire " e "Traffic
sns.countplot(x='Reason', data = df)



# %% Bloco 02: informações de tempo
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

# Com base na coluna timeStamp use .apply () para criar 3 novas colunas chamadas Hour, Month e Day of Week
df['Hour'] = df['timeStamp'].apply(lambda x: x.hour)
df['Month'] = df['timeStamp'].apply(lambda x: x.month)
df['Day of Week'] = df['timeStamp'].apply(lambda x: x.dayofweek)

# %% Bloco 03: Use o .map () com este dicionário para mapear os nomes das sequências reais para o dia da semana
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)
df['Day of Week']



# %% Bloco 04: countplot da coluna "Day of Week"
sns.countplot(x='Day of Week', data=df, hue='Reason', palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # Ajuste a posição da legenda conforme necessário



# %% Bloco 05: countplot da coluna mês
sns.countplot(x='Month', data=df, hue='Reason', palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)




# %% Bloco 06: Objeto groupby chamado "byMonth"
byMonth = df.groupby("Month").count()
byMonth.head(12)


# %% Bloco 07: plot simples indicando a contagem de chamadas por mês
byMonth['twp'].plot() 



# %% Bloco 08: modelo linear
byMonth.reset_index()
sns.lmplot(x='Month', y='twp', data=byMonth.reset_index())



# %% Bloco 09: Gráfico de contagem de camadas por dia
df['Data'] = df['timeStamp'].apply(lambda x:x.date())
df.groupby('Data').count()
df.groupby('Data').count()['twp'].plot()
plt.xticks(rotation=45)




# %% Bloco 10: 3 plots - cada plot para um tipo de ocorrência
# %% Traffic
df[df['Reason']=='Traffic'].groupby('Data').count()['twp'].plot()
plt.xticks(rotation=45)


# %% Bloco 11: Fire
df[df['Reason']=='Fire'].groupby('Data').count()['twp'].plot()
plt.xticks(rotation=45)


# %% Bloco 12: EMS
df[df['Reason']=='EMS'].groupby('Data').count()['twp'].plot()
plt.xticks(rotation=45)


# %% Bloco 13: Criando indice multinível
dayHour = df.groupby(by = ['Day of Week', 'Hour']).count()['twp']. unstack()
dayHour


# %% Bloco 14: mapa de calor usando este DataFrame(dayHour)
plt.figure(figsize=[12, 6]) #ajustar tamanho
sns.heatmap(dayHour)


# %% Bloco 15: 
sns.clustermap(dayHour)


# %% Bloco 16: clustermap para o DataFrame que mostra o mês como a coluna
dayMonth = df.groupby(by = ['Day of Week', 'Month']).count()['twp']. unstack()
plt.figure(figsize=[12, 6])
sns.heatmap(dayMonth)


# %% Bloco 17: 
sns.clustermap(dayMonth)
