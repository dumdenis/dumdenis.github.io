#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:04:44 2021

@author: denisdumont
"""
###############################################################################
#Dice or Coin throws : Calulate "N_mean" means over "N_throw" throws of dice
#and verify the expected normal law distribution
###############################################################################

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from collections import Counter

N=10000 #Nombre de moyenne
n=1000 #Nombre de lancer
m=24 #Nombre de face du dé (2 pour une pièce)

#QUESTIONS 1 et 2
lancers=np.random.randint(1,m+1,n)
moyenne=np.mean(lancers)
print(moyenne)
print(Counter(lancers))

#QUESTION 3 et 4
N=10000
n=1000

list_moyenne=[]
for i in np.arange(1,N):
    lancers=np.random.randint(1,m+1,n)
    moyenne=np.mean(lancers)
    list_moyenne.append(moyenne)

prob,interv=np.histogram(list_moyenne,bins='auto',density=True)
#Milieu de chaque interval
mid_interv=[(interv[i]+interv[i+1])/2. for i in range(len(interv)-1)]
#Graphique
plt.figure(1)
plt.plot(mid_interv,prob,'o')
plt.xlabel('Value')
plt.ylabel('Probability')

#Definition de la fonction gaussienne
def gauss(x,a,mu,sigma):
    return a*np.exp(-1/2*((x-mu)/sigma)**2)

#Ajsutement et plot en graphique
popt,pcov=curve_fit(gauss,mid_interv,prob,p0=[1/(np.sqrt(np.var(np.arange(1,m+1)))*np.sqrt(2*np.pi)),np.mean(np.arange(1,m+1)),0.1])#Need to adjust p0 to help the fit,by default p0=[1,1,1]
plt.plot(mid_interv,gauss(mid_interv, *popt),'r-',label='Fit: a=%5.3f, mu=%5.3f, sigma=%5.3f' % tuple(popt))

#Graph prediction theoriques
Mean_theo= np.mean(np.arange(1,m+1)) #Calculation of the theoretical mean
Sigma_x=np.sqrt(np.var(np.arange(1,m+1)))
Sigma_theo=Sigma_x/np.sqrt(n) #Calculation of the theoretical standard deviation
x=np.linspace(Mean_theo-3*Sigma_theo,Mean_theo+3*Sigma_theo)
lab="Pred theo: a="+str(round(1/(Sigma_theo*np.sqrt(2*np.pi)),2))+str(round(Mean_theo,2))+", mu="+str(round(Mean_theo,2))+", sigma="+str(round(Sigma_theo,3))
plt.plot(x,gauss(x,1/(Sigma_theo*np.sqrt(2*np.pi)),Mean_theo,Sigma_theo),'g-.',label=lab)
plt.legend()
plt.show()

#QUESTION 5
list_n=[1000,10000,100000]
list_sigma=[]
for j in list_n:
    list_moyenne=[]
    for i in np.arange(1,N):
        lancers=np.random.randint(1,m+1,j)
        moyenne=np.mean(lancers)
        list_moyenne.append(moyenne)

    prob,interv=np.histogram(list_moyenne,bins='auto',density=True)
    #Milieu de chaque interval
    mid_interv=[(interv[i]+interv[i+1])/2. for i in range(len(interv)-1)]
    #Graphique
    plt.figure(2)
    plt.plot(mid_interv,prob,'o')
    plt.xlabel('Value')
    plt.ylabel('Probability')

    #Definition de la fonction gaussienne
    def gauss(x,a,mu,sigma):
        return a*np.exp(-1/2*((x-mu)/sigma)**2)

    #Ajsutement et plot en graphique
    popt,pcov=curve_fit(gauss,mid_interv,prob,p0=[1/(np.sqrt(np.var(np.arange(1,m+1)))*np.sqrt(2*np.pi)),np.mean(np.arange(1,m+1)),0.1])#Need to adjust p0 to help the fit,by default p0=[1,1,1]
    plt.plot(mid_interv,gauss(mid_interv, *popt),'r-',label='Fit: a=%5.3f, mu=%5.3f, sigma=%5.3f' % tuple(popt))
    list_sigma.append(abs(popt[2]))

plt.figure(3)
plt.loglog(list_n,list_sigma,'o',label='data')
plt.loglog(list_n,1/np.sqrt(np.array(list_n)),label='1/n**0.5')
plt.legend()
#Plus on augmente n plus la valeur moyenne ets précise + on observe bien une
#evolution en 1/n^0.5 de l'ecart type comme vu au cours theorique(cfr. figur 3)

#QUESTIONS 6 et 7
#mettre m=6 et m=24