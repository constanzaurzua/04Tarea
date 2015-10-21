#Runge-Kutta

import numpy as np
import matplotlib.pyplot as plt
from planeta import Planeta

'''Calculo con RK4'''

condicion_inicial=[10, 0 , 0 ,0.4]
p = Planeta(condicion_inicial)
pasos = 16500
dt = 8000./pasos
t = np.linspace(0,8000,pasos)

x=np.zeros(pasos)
y=np.zeros(pasos)
e=np.zeros(pasos)

x[0]=10
y[0]=0
e[0]=p.energia_total()

for i in range(1,pasos):
    x[i]= p.y_actual[0]
    y[i]= p.y_actual[1]
    e[i]=p.energia_total()
    p.avanza_rk4(dt)
    p.energia_total()

plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.xlabel('$X$', fontsize=15)
plt.ylabel('$Y$',fontsize=15)
plt.title('$\ Metodo \ Runge-Kutta \ con \ alpha = 0$')
plt.plot(x,y)
plt.subplot(212)             # the second subplot in the first figure
plt.xlabel('$\ tiempo\ [s]$', fontsize=15)
plt.ylabel('$Energia$',fontsize=15)
plt.title('$\ Energia \ en \ funcion \ del \ tiempo$')
plt.plot(t,e)
plt.savefig('fig1.png')
plt.show()
