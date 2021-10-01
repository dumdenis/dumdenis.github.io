#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 17:26:15 2018

@author: dumontdenis
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

###################### GENERATION DE NOMBRE ALEATOIRES #######################

#Generation de nombres aleatoires entiers
resultat1=np.random.randint(1,7,10)
#Calcul de la moyenne
moyenne=np.mean(resultat1)
#moyenne_theorique=(1+2+3+4+5+6)/6
moyenne_theorique=np.sum(np.arange(1,7))/6
#Calcul de la variance
variance=np.var(resultat1)

#Generation de nombres aleatoires dans une liste d'elements
resultat2=np.random.choice([-1,1,4,6],10)

#Generation de nombress aleatoires suivant une loi de probabilite uniforme
resultat3=np.random.uniform(-1,1,10)

resultat4=np.random.normal(2,0.5,10)

#Il existe de nombreuses autres fonctions generant des nombres aleatoires,Tips:
#regarder la documentation disponible en ligne de la librairie numpy.random

##################### FAIRE UN GRAPHIQUE AVEC MATPLOTLIB ######################

#Generations de donnees aleatoires en vue de faire un graphique
data_list=[]
for i in np.arange(1,11):
    data=i+np.random.uniform(-1,1)
    data_list.append(data)

#Methode alternatives pour la boucle
data_list=[]
i=1
while i < 11:
    data=i+np.random.uniform(-1,1)
    data_list.append(data) 
    i+=1

#Graphique
plt.figure(1)
plt.xlim(0,11)
plt.ylim(0,11)
plt.plot(np.arange(1,11),data_list,'o',label='test')
plt.xlabel("Name_x")
plt.ylabel("Name_y")
plt.grid(True)

##################### AJUSTER UNE COURBE A DES DONNEES #######################


#Definition de la fonction lineaire
def linear(x,a,b):
    '''linear function in order to fit data'''
    return a*x+b
 
#Ajsutement et plot en graphique
popt,pcov=curve_fit(linear,range(1,11),data_list)
plt.plot(np.arange(1,11),linear(np.arange(1,11),*popt),'-',label='a='+str(popt[0])+",b="+str(popt[1]))
plt.legend()
plt.show()

################################ HISTOGRAMMES #################################

#Generation de nombress aleatoires suivant une loi de probabilite gaussienne
data=np.random.normal(2,0.5,10000)
#Generation de l'histogramme
prob,interv=np.histogram(data,bins='auto',density=True)
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
popt,pcov=curve_fit(gauss,mid_interv,prob,p0=[1,2,0.5])#Need to adjust p0 to help the fit,by default p0=[1,1,1]
plt.plot(mid_interv,gauss(mid_interv, *popt),'r-',label='Fit: a=%5.3f, mu=%5.3f, sigma=%5.3f' % tuple(popt))
plt.legend()
plt.show()