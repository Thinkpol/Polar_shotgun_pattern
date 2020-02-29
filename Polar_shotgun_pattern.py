#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 11:08:44 2020

@author: Matthieu LEROY

https://github.com/Thinkpol
"""

import matplotlib.pyplot as plt
import numpy as np

def asym_lemniscate(T, a, b, c=1):
    '''
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
    y = a*(np.cos(T)+b)*np.cos(T)*np.sin(T) / (1+np.sin(T)**2)
    return np.sqrt(x**2 + y**2)


T = np.linspace(-np.pi, np.pi, 1000)

fig = plt.figure()

ax = plt.subplot(1, 1, 1, projection="polar")
ax.plot(T, asym_lemniscate(T, 1, 0.3, 0.15), color='tab:orange')
ax.plot(T, asym_lemniscate(T-np.pi/2, 0.4, 0, 0.15), color='tab:orange')
ax.set_theta_offset(np.pi/2)

fig.savefig('/Users/Matthieu/Polar_shotgun_pattern.png', dpi=72)

