# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:52:41 2023

@author: Diego
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv("911.csv")

#Verifique a info() do df
df.info()

#Verifique o cabeçalho do df
df.head(5)

#Os 5 ceps com maior número de chamadas
df['zip'].value_counts().head(5)

#Os 5 municípios com maior número de chamadas
df['twp'].value_counts().head(5)

#Quantos códigos de título 'exclusivos' existem(código é um tipo de ocorrência)
df['title'].nunique()

#Criar uma nova coluna chamada ('Reason') com os tipos de ocorrência "EMS(Serviços Médicos de Emergência)", "Fire (serviços de combate a incêndios) " e "Traffic(Serviços de emergência de Tráfego)"
#Nova coluna
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])
df['Reason']

#Ocorrência mais comum para uma chamada do 911
df['Reason'].value_counts()
