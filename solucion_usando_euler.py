#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from planeta import Planeta


condicion_inicial=[10.0, 0 , 0 ,0.4]
p = Planeta(condicion_inicial)
pasos = 16500
dt = 8000./pasos
t = np.linspace(0,8000,pasos)

x=np.zeros(pasos)
y=np.zeros(pasos)
e=np.zeros(pasos)

x[0]= 10
y[0]= 0
e[0]=p.energia_total()

for i in range(1,pasos):
    p.avanza_euler(dt)
    x[i]= p.y_actual[0]
    y[i]= p.y_actual[1]
    e[i]=p.energia_total()
    p.energia_total()

print e
plt.figure(1)
plt.plot(x,y)
plt.show()

plt.figure(2)
plt.plot(t,e)
plt.show()

'''ax1 = fig.add_subplot(211)
plt.suptitle('Trayectoria y energia vs tiempo con $v_{y}(t=0)=0.4$ y  ' r'$\alpha=0$ (Euler explicito)')
fig.subplots_adjust(hspace=.3)
ax1.plot(x,y)
ax1.grid(True)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax2 = fig.add_subplot(212)
ax2.plot(t,e)
ax2.grid(True)
ax2.set_xlabel('tiempo')
ax2.set_ylabel('energia')
ax2.set_ylim(-0.03,-0.01)



plt.draw()
plt.show()'''
