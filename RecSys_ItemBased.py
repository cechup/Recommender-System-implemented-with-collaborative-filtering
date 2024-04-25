# -*- coding: utf-8 -*-
"""
Created on Sun May 22 10:39:05 2022

@author: pecco
"""

import pandas as pd
import numpy as np
# import numpy.ma as ma
from scipy import spatial
#import math
import random

################################################
database = pd.read_csv('Data.csv')


# CREAZIONE MATRICE USER-ITEM
user_item = pd.pivot_table(database, values='rating',index='userId',
                            columns='title')
user_item = user_item.replace(np.nan,0.0)
# matrice molto sparsa, obiettivo è stimare ratings dove c'è valore mancante


# CLASSE
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
    
    def create_ord_list(rate,rate_dict):
        ord_list = sorted(rate_dict.items(), key=lambda x: x[1],
                          reverse = True)
        u = int(input("Inserire numero Id utente: "))
        titles_list = []
        for i in range(len(ord_list)):
            if ord_list[i][0][0] == u :
                index = ord_list[i][0][1]
                titles_list.append(rate.title[index])
        return titles_list[1:30]
    
    
r = Rate(user_item.values,user_item.index,user_item.columns)


# CREAZIONE ARRAY
user_item_m = Rate.create_table(r)

tot = user_item_m.shape[0]*user_item_m.shape[1]    
sparsità = np.count_nonzero(user_item_m==0)
non_zero = tot - sparsità
tot_test = int(np.round(non_zero * 0.25))


# VALORI DA MATRICE A DIZIONARIO
def fun_to_dic(m):
    dic = {}
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if m[i,j] > 0:
                # adding non zero elements to
                # the dictionary
                dic[i, j] = m[i,j] 
    return dic


data_dict = fun_to_dic(user_item_m)
Keys = data_dict.keys()
ListOfKeys = list(Keys)

random.seed(10)
#rnd = [random.randrange(0, len(ListOfKeys)) for u in range(0, tot_test)]
rnd = random.sample(ListOfKeys, tot_test)

ui_m = user_item_m.copy()


def create_test_table(rand):
    test = np.zeros(([ui_m.shape[0],ui_m.shape[1]]),dtype=float)
    for i in range(len(rand)):
        u = rand[i]
        test[u] = user_item_m[u]
        ui_m[u] = 0
    return test


test_m = create_test_table(rnd)   
non_zero_test = np.count_nonzero(ui_m==0)
tot - non_zero_test
test_dict = fun_to_dic(test_m)   



def similarity(vect1,vect2):
    v1 = vect1[0,:]
    v2 = vect2[0,:]
    # l1 = []
    # l2 = []
    r = 1-spatial.distance.cosine(v1,v2)
    return np.round(r,2)
    #return np.dot(v1.T, v2) / np.dot(math.sqrt(np.dot(v1.T,v1)),math.sqrt(np.dot(v2.T,v2)))
    # for i in range(len(v1)):
    #     if v1[i] > 0 and v2[i] > 0:
    #         l1.append(v1[i])
    #         l2.append(v2[i])
    # corr = np.corrcoef(l1,l2)
    # return np.round(corr[0,1],2)


def distances(m): 
    d = np.zeros(([m.shape[1],m.shape[1]]),dtype=float)
    for j in range(m.shape[1]):
        for i in range(m.shape[1]):
            if i != j:
                d[j,i] = similarity(m[j:j+1,:],m[i:i+1,:])
            else :
                d[j,i]=0
        print(j)
    return d # mi ritorna matrice u x u in cui diagonale è 0, altri incroci
# sono quanto u_i e u_j si somigliano. Dovrebbe essere matrice triangolare


# ora stimo valori mancanti della matrice user_item
def media_pond(pesi,valori):
    num = 0.0
    den = 0.0 
    for j in range(len(valori)):
        if valori[j] > 0 and pesi[j] > 0:
            num = num + pesi[j]*valori[j]
            den = den + pesi[j]
    try:
        ret=num/den
    except Exception as e:
        print (e)
        ret=0
    return ret



    
def fit_zero_ratings(t,d): 
        st = np.zeros(([t.shape[0],t.shape[1]]),dtype=float)
        for i in range(t.shape[1]):
            for j in range(t.shape[0]):
                if t[j,i] == 0:
                    st[j,i] = media_pond(d[:,i], t[j,:].T)
            print(i)
        return st                    
            
    

# CALCOLI

dist = distances(ui_m)
fit_val = fit_zero_ratings(ui_m,dist)

np.savetxt('ItemBased_Fitted.txt',fit_val)

fit_dict = fun_to_dic(fit_val)


def mse(m,st,n): # t è matrice user-item test e st sono valori stimati 
    err = 0
    row = m.shape[0]
    col = m.shape[1]
    for i in range(row):
        for j in range(col):
            if m[i,j] > 0:
                err = err + (m[i,j]-st[i,j])**2
    return err/n

mse_test = mse(test_m,fit_val,tot_test)
