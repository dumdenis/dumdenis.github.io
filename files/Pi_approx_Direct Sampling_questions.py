#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 09:55:36 2021

@author: denisdumont
"""

import random as rd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#Question1 a 3
N_throws=10000
N_hit=0
listx_in,listy_in=[],[]
listx_out,listy_out=[],[]
for i in range(N_throws):
    x,y=np.random.random(),np.random.random()
    if np.sqrt(x**2+y**2)<1:
        N_hit+=1
        listx_in.append(x),listy_in.append(y)
    else:
        listx_out.append(x),listy_out.append(y)
print((N_hit/N_throws)*4)
plt.figure(1)
plt.plot(listx_in,listy_in,'o')
plt.plot(listx_out,listy_out,'o')

#Question 4
def gauss(x,a,mu,sigma):
    '''Gaussian function in order to fit data'''
    return a*np.exp(-1/2*((x-mu)/sigma)**2)

N_try=1000
N_throws=1000
list_approx=[]
for j in range(N_try):
    N_hit=0   
    for i in range(N_throws):
        x,y=np.random.random(),np.random.random()
        if np.sqrt(x**2+y**2)<1:
            N_hit+=1            
    approx=(N_hit/N_throws)*4
    list_approx.append(approx)
    
plt.figure(2)
plt.hist(list_approx,bins='auto',density=True,alpha=0.75)
prob,interv=np.histogram(list_approx,bins='auto',density=True)
mid_interv=[(interv[i]+interv[i+1])/2. for i in range(len(interv)-1)]
plt.plot(mid_interv,prob,'o')
popt,pcov=curve_fit(gauss,mid_interv,prob)
plt.plot(mid_interv,gauss(mid_interv, *popt),'r-',label='Fit: a=%5.3f, mu=%5.3f, sigma=%5.3f' % tuple(popt))
plt.xlabel('Position')
plt.ylabel('Probability')
plt.legend(loc='best')

#Question 5
list_mean_deviation=[]
listN_throws=[10**n for n in range(1,5)]
N_try=100
for N_throws in listN_throws :
    print("########## N_Trials="+str(N_try)+" ##########")
    list_approx,list_deviation=[],[]
    for i in range(N_try):
        N_hits=0
        for i in range(N_throws):
            x,y = rd.random(),rd.random() #Random hit
            if np.sqrt(x**2+y**2)<1: #Check if the hit is inside the circle
                N_hits+=1
        approx_pi=N_hits/N_throws*4 #Give an approximation of pi
        list_approx.append(approx_pi)
        list_deviation.append((approx_pi-np.pi)**2)
    list_mean_deviation.append(np.mean(list_deviation))
plt.figure(3)
plt.xscale("log")
plt.yscale("log")
plt.plot(listN_throws,np.sqrt(list_mean_deviation),'o',label="Simulation Results")
plt.plot(listN_throws,1/np.sqrt(np.array(listN_throws)),label="1/N^0.5")
plt.xlabel("N trials")
plt.ylabel("Root Mean Square Deviation")
plt.legend()





