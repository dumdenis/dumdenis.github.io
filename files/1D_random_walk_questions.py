#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 17:26:15 2018

@author: dumontdenis
"""
import matplotlib.pyplot as plt
import random as rd
import numpy as np
from scipy.optimize import curve_fit

def lin(x,a):
    '''linear function in order to fit data'''
    return a*x

def gauss(x,a,mu,sigma):
    '''gaussian function in order to fit data'''
    return a*np.exp(-1/2*((x-mu)/sigma)**2)

#QUESTION1
n_step=10
pos=0 #Initial position
hist_pos=[pos] #History of the position during the whole walk
for i in range(n_step):
    step=rd.choice([-1,1]) #Random step
    pos+=step #Update of new position
    hist_pos.append(pos) #Storage of new position in the history
#Plot the walk
plt.figure(1)
plt.ylim(-n_step-1,n_step+1)
plt.plot(range(n_step+1),hist_pos)
plt.plot(range(n_step+1),hist_pos,'og')
plt.xlabel("Steps")
plt.ylabel("Position")
plt.grid(True)

#QUESTION2,6 et 7
n_step=1000
n_walker=1000
hist_pos_all=[]#Memory containing every try
for j in range(n_walker):
    pos,hist_pos=0,[0] #Initial position, history of the position
    for i in range(n_step):
        step=rd.choice([-1,1]) #Random step
        pos+=step #Update of new position
        hist_pos.append(pos) #Storage of new position in the history
    hist_pos_all.append(hist_pos) #Storage of new walk in the history
    #Plot the walk
    plt.figure(2)
    #plt.ylim(-n_step-1,n_step+1)
    plt.plot(range(n_step+1),hist_pos)
    plt.xlabel("Steps")
    plt.ylabel("Position")
    plt.grid(True)

#Plot of <x>
plt.figure(2)
plt.xlabel('t(# steps)')
plt.ylabel('<x>')
plt.plot(np.arange(n_step+1),np.mean(hist_pos_all,axis=0),'r',linewidth=5)
#Plot of <x^2>
plt.figure(4)
plt.xlabel('t(# steps)')
plt.ylabel('<x^2>')
plt.plot(np.arange(n_step+1),np.mean(np.array(hist_pos_all)**2,axis=0),label='Random walk')
#Linear fit of <x^2>
popt,pcov=curve_fit(lin,np.arange(n_step+1),np.mean(np.array(hist_pos_all)**2,axis=0))
lab=str(round(popt[0]/2,2))
plt.plot(np.arange(n_step+1),lin(np.arange(n_step+1),*popt),'-',label='D='+lab)
plt.legend()

#QUESTION3
n_step=6
n_walker=1000
last_pos=[] #Last position of all the "n_walker" walkers
for j in range(n_walker):
    pos=0 #Initial position
    for i in range(n_step):
        step=rd.choice([-1,1]) #Random step
        pos+=step #Update of new position
    last_pos.append(pos) #Storage of new position in the history
#Plot the distribution
plt.figure(5)
plt.hist(last_pos,200,density=False,facecolor='g',alpha=0.75)
plt.xlabel('Position')
plt.ylabel('Prob')

plt.xlim(-7,7)
pred_theo=np.array([1/64,6/64,15/64,20/64,15/64,6/64,1/64])*n_walker#Triangle de Pascal
plt.plot([-6,-4,-2,0,2,4,6],pred_theo,'o', label="Theoretical predictions")
plt.legend()

#QUESTION4
n_step=1000
n_walker=10000
last_pos=[] #Last position of all the "n_walker" walkers
for j in range(n_walker):
    pos=0 #Initial position
    for i in range(n_step):
        step=rd.choice([-1,1]) #Random step
        pos+=step #Update of new position
    last_pos.append(pos) #Storage of new position in the history
#Plot the distribution
plt.figure(6)
plt.hist(last_pos,200,density=False,facecolor='g',alpha=0.75)
plt.xlabel('Position')
plt.ylabel('Prob')

#Probability density
prob,interv=np.histogram(last_pos,bins='auto',density=True)
#Middle of each interval
mid_interv=[(interv[i]+interv[i+1])/2. for i in range(len(interv)-1)]
#Graph
plt.figure(7)
plt.plot(mid_interv,prob,'o')
popt,pcov=curve_fit(gauss,mid_interv,prob,p0=[0.01,0,30])#Need to adjust p0 to help the fit,by default p0=[1,1,1]
plt.plot(mid_interv,gauss(mid_interv, *popt),'r-',label='Fit: a=%5.3f, mu=%5.3f, sigma=%5.3f' % tuple(popt))
plt.xlabel('Position')
plt.ylabel('Probability')
plt.legend(loc='best')