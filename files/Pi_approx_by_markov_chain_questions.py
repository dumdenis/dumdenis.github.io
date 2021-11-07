#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 10:37:25 2021

@author: denisdumont
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Questions 1 et 2
N_steps=1000
delta=0.5
x,y=0,0
N_hits=0
listx,listy=[x],[y]
for i in range(N_steps):
    dx=np.random.uniform(-delta,delta)
    dy=np.random.uniform(-delta,delta)
    if abs(x+dx)<=1 and abs(y+dy)<=1: 
        x+=dx
        y+=dy
    if (x**2+y**2)<1: #Check if the new position is inside the circle
        N_hits+=1
    listx.append(x)
    listy.append(y)
print(4*N_hits/N_steps)

plt.figure(0)
plt.plot(listx,listy)
ax=plt.subplot(aspect='equal')
plt.axis((-1,1,-1,1))
plt.plot(listx,listy,'k-')
plt.plot(listx,listy,'ro')
circle=plt.Circle((0,0),1,color='b',fill=True)
ax.add_artist(circle)

#Questions 3
N_try=1000
N_steps=1000
delta=0.5
list_approx=[]
for j in range(N_try):
    x,y=0,0
    N_hits=0
    listx,listy=[x],[y]
    for i in range(N_steps):
        dx=np.random.uniform(-delta,delta)
        dy=np.random.uniform(-delta,delta)
        if abs(x+dx)<=1 and abs(y+dy)<=1: 
            x+=dx
            y+=dy
        if (x**2+y**2)<1: #Check if the new position is inside the circle
            N_hits+=1
    approx=4*N_hits/N_steps
    list_approx.append(approx)

def gauss(x,a,mu,sigma):
    '''Gaussian function in order to fit data'''
    return a*np.exp(-1/2*((x-mu)/sigma)**2)

plt.figure(1)
plt.hist(list_approx,bins=50,density=True,alpha=0.75)
#Probability density
prob,interv=np.histogram(list_approx,bins='auto',density=True)
#Middle of each interval
mid_interv=[(interv[i]+interv[i+1])/2. for i in range(len(interv)-1)]
#Graph
plt.figure(1)
plt.plot(mid_interv,prob,'o')
popt,pcov=curve_fit(gauss,mid_interv,prob)
plt.plot(mid_interv,gauss(mid_interv, *popt),'r-',label='Fit: a=%5.3f, mu=%5.3f, sigma=%5.3f' % tuple(popt))
plt.xlabel('Position')
plt.ylabel('Probability')
plt.legend(loc='best')

#Questions 4
N_try=100
listN_steps=[10**n for n in range(1,5)]
delta=0.5
list_mean_deviation=[]
for N_steps in listN_steps:
    print(N_steps)
    list_approx=[]
    list_deviation=[]
    for j in range(N_try):
        x,y=0,0
        N_hits=0
        listx,listy=[x],[y]
        for i in range(N_steps):
            dx=np.random.uniform(-delta,delta)
            dy=np.random.uniform(-delta,delta)
            if abs(x+dx)<=1 and abs(y+dy)<=1: 
                x+=dx
                y+=dy
            if (x**2+y**2)<1: #Check if the new position is inside the circle
                N_hits+=1
        approx=4*N_hits/N_steps
        list_approx.append(approx)
        list_deviation.append((approx-np.pi)**2)
    list_mean_deviation.append(np.mean(list_deviation))
plt.figure(3)
plt.xscale("log")
plt.yscale("log")
plt.plot(listN_steps,np.sqrt(list_mean_deviation),'o',label="Simulation Results")
plt.plot(listN_steps,1/np.sqrt(np.array(listN_steps)),label="1/N^0.5")
plt.xlabel("N trials")
plt.ylabel("Root Mean Square Deviation")
plt.legend()

#Questions 5
#En changeant la valeur de x et y dans la question 1, on retouve tpoujours la
#bonne approximation de pi.

#Questions 6 et 7
N_steps=1000
N_try=100
list_delta=[0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,2,3]
list_mean_deviation,list_mean_accept_rate=[],[]
for delta in list_delta :
    print("########## Delta="+str(delta)+" ##########")
    list_deviation,list_accept_rate=[],[]
    for i in range(N_try):
        N_hits,accepted=0,0
        x,y=0,0
        for j in range(N_steps):
            dx=np.random.uniform(-delta,delta)
            dy=np.random.uniform(-delta,delta)
            if abs(x+dx)<1 and abs(y+dy)<1:
                x+=dx
                y+=dy
                accepted+=1
            if (x**2+y**2)<1:
                N_hits+=1
        approx=4*N_hits/N_steps
        accept=accepted/N_steps 
        deviation=(approx-np.pi)**2
        list_deviation.append(deviation)
        list_accept_rate.append(accept)
    list_mean_deviation.append(np.mean(deviation))
    list_mean_accept_rate.append(np.mean(list_accept_rate))
#Graph of the Root mean square dev
plt.figure(4)
plt.plot(list_delta,list_mean_deviation,'o',label="Simulation Results")
plt.xlabel("Delta")
plt.ylabel("Deviation")
plt.legend()
#Graph of the Acceptance Rate
plt.figure(5)
plt.plot(list_delta,list_mean_accept_rate,'o',label="Simulation Results")
plt.xlabel("Delta")
plt.ylabel("Acceptance rate")
plt.legend()   