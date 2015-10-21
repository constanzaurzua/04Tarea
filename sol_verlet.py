import numpy as np
import matplotlib.pyplot as plt
from planeta import Planeta

condicion_inicial = [10, 0, 0, 0.3] #x, y, vx, vy

p = Planeta(condicion_inicial) #se establece condicio inicial como actuales
pasos=8000
dt=4000./pasos
t=np.linspace(0,4000,pasos)#aproximadamente 5 orbitas
# se crean listas vacias de x, y, Energia
x=np.zeros(pasos)
y=np.zeros(pasos)
e=np.zeros(pasos)
#Se agregan condiciones iniciales
x[0]=0
y[0]=0
e[0]=p.energia_total()

for i in range(1,pasos):
    p.avanza_verlet(dt)
    x[i]=p.y_actual[0]
    y[i]=p.y_actual[1]
    e[i]=p.energia_total()
    p.energia_total()

    #Energia.append(p.energia_total())


plt.figure(1)


'''ax1 = fig.add_subplot(311)
plt.suptitle('Trayectoria y energia vs tiempo con $v_{y}(t=0)=0.4$ y  ' r'$\alpha=0$ (Verlet)')
fig.subplots_adjust(hspace=.3)'''

plt.plot(x,y)
'''ax1.set_xlim(-45,15)
ax1.grid(True)
ax1.set_xlabel('x')
ax1.set_ylabel('y')'''
plt.show()
plt.figure(2)
plt.plot(t,e)
plt.show()
