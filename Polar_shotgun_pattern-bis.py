#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 16:49:38 2020

@author: Matthieu LEROY
"""

import numpy as np
import matplotlib.pyplot as plt

def asym_lemniscate(T, a, b, c=1, d=1):
    '''
    https://www.jneurosci.org/content/22/18/8201
    
    T: float
        Angle between -pi and pi.
    a: flaot
        Amplitude.
    b: float
        Asymetric paramter.
    c: float
        Squish parameter.
    '''
    x = a*(np.cos(T)+b)*np.cos(T) / (c+np.sin(T)**2)
#    y = a*(np.cos(T)+b)*np.cos(T)*np.sin(T) / (c+np.sin(T)**2)
    y = d*x*np.sin(T)
    res = np.sqrt(x**2 + y**2)
    return np.exp(res)/10000

def plot(ax, title, alpha=1, shotgun=False):
    T = np.linspace(-np.pi, np.pi, 5000)
    if shotgun:
        R = asym_lemniscate(T, 4, 0.2, 0.1, 4) + \
            asym_lemniscate(T-np.pi/2, 11, 0, 0.5)
        
    else:
        R = alpha + (1-alpha)*np.cos(T)
    R = np.log(1+np.abs(50*R)) / np.log(10)
    R = 1000*(R/R.max())
    
    ax.set_theta_offset(np.pi/2)
    ax.set_thetalim(0,2*np.pi)
    ax.set_rorigin(0)
    ax.set_rlabel_position(np.pi/2)

    ax.fill(T, R, zorder=20,
            color="C1", clip_on=True, alpha=0.25)
    ax.plot(T, R, zorder=30, alpha=0.75, 
            color="C1", linewidth=1.0, linestyle=":", clip_on=False)
    ax.plot(T, R, zorder=40,
            color="C1", linewidth=1.5, clip_on=True)
    ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2])
    ax.xaxis.set_tick_params("major", pad=-2.5)
    ax.set_xticklabels(["0°", "","180°",""], family="Roboto", size="small",
                       horizontalalignment = 'center',
                       verticalalignment = 'center')
    ax.set_yticks([200, 400, 600, 800, 1010])

    for y,label in zip([390,590,790], ["-20dB", "-15dB", "-10dB"]):
        ax.text(0, y, label, zorder=10,
                family="Roboto Condensed", size="small",
                horizontalalignment = 'center', verticalalignment = 'center',
                bbox=dict(facecolor='white', edgecolor="None", pad=1.0))
    ax.set_yticklabels([])

    ax.set_ylim(200,1010)
    ax.set_title(title, family="Roboto", weight="bold", size="large", y=-0.2)

fig = plt.figure(figsize=(8,7))
fig.suptitle("Microphone polar patterns",
             family="Roboto", weight="bold", size="xx-large")

# Shotgun (not quite right yet)
ax = plt.subplot(1, 1, 1, projection="polar")
plot(ax, "Shotgun", shotgun=True)


plt.tight_layout()
plt.savefig("polar-patterns.pdf")
plt.show()