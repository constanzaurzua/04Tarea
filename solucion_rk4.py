#Runge-Kutta

import numpy as np
import matplotlib.pyplot as plt
from planeta import Planeta

condicion_inicial=[10, 0 , 0 ,0.4]
p = Planeta(condicion_inicial)
pasos = 10000#4*np.int(1e3)
dt = 0.1#2000./pasos
t = np.linspace(0,2000,pasos)

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

plt.figure(1)
plt.plot(x,y)
plt.show()
plt.figure(2)
plt.plot(t,e)
plt.show()
