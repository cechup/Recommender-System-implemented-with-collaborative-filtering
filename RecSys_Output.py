1# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 20:02:32 2022

@author: pecco
"""

import pandas as pd
import numpy as np


database = pd.read_csv('Data.csv')

# CREAZIONE MATRICE USER-ITEM
data = pd.pivot_table(database, values='rating',index='userId',
                            columns='title')
data = data.replace(np.nan,0.0)

fitted_values_i = np.loadtxt('ItemBased_Fitted.txt')
fitted_values_u = np.loadtxt('UserBased_Fitted.txt')


class Rate:
    def __init__(rate,value,userId,title):
        rate.value = value
        rate.user = userId
        #rate.movie = movieId
        rate.title = title
        
    def create_table(rate):
        v = rate.value
        t = np.array(v)
        return t
    
    def create_ord_list(rate,rate_dict,u):
        ord_list = sorted(rate_dict.items(), key=lambda x: x[1],
                          reverse = True)
        titles_list = []
        u_ind = 0
        for i in range(len(rate.user)):
            if r.user[i] == u:
                u_ind = i
        if u_ind == 0 and u != 2:
            print("Utente non presente. Riprovare")
        else: 
            for i in range(len(ord_list)):
                if ord_list[i][0][0] == u_ind :
                    index = ord_list[i][0][1]
                    titles_list.append(rate.title[index])
            return titles_list[0:29]
        

r = Rate(data.values,data.index,data.columns)
        
    
def fun_to_dic(m):
    dic = {}
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if m[i,j] != 0:
                # adding non zero elements to
                # the dictionary
                dic[i, j] = m[i,j] 
    return dic


data_dict = fun_to_dic(fitted_values_i)

u = int(input("Inserire numero Id utente: "))
l = r.create_ord_list(data_dict,u)
output = '\n\n LISTA DEI PRIMI 30 FILM RACCOMANDATI PER UTENTE CON ID ' + repr(u) + ': \n'
print(output,l)

        