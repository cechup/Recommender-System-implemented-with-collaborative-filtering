# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:22:18 2022

@author: pecco
"""

############################################
import pandas as pd
import numpy as np


# ORGANIZZAZIONE DATI
# da GroupLens, MovieLens
data = pd.read_csv("ratings.csv")
movies = pd.read_csv("movies.csv")

data1 = data.merge(movies,on='movieId', how='left')

data_base = data1.loc[data['userId']<=5000]
v_item = data_base[['movieId']]
data_base = data_base[v_item.replace(v_item.stack().value_counts()).gt(500).all(1)]
v_user = data_base[['userId']]
data_base = data_base[v_user.replace(v_user.stack().value_counts()).gt(50).all(1)]


# ho preso primi 5000 utenti e da questi ho tolto utenti che avevano messo
# meno di 50 ratings e film che avevano meno di 500 voti

# dati in formato lungo

data_base.to_csv('Data.csv',index=False)


