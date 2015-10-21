from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt

condicion_inicial = [10, 0, 0, 0.4]
p = Planeta(condicion_inicial, 10**(-2.487))

pasos= 16500*6
dt=8000*6./pasos
t=np.linspace(0,8000*6,pasos)

x= np.zeros(pasos)
y= np.zeros(pasos)
e = np.zeros(pasos)

x[0]= 10
y[0]= 0
e[0]=p.energia_total()

for i in range(1, pasos):
    p.avanza_verlet(dt)
    x[i]=p.y_actual[0]
    y[i]=p.y_actual[1]
    p.energia_total()
    e[i]=p.energia_total()

plt.figure(1)
plt.plot(x,y)
plt.show()

plt.figure(2)
plt.plot(t,e)
plt.show()
