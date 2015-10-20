#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Planeta(object):
    '''
    Complete el docstring.
    '''

    def __init__(self, condicion_inicial, alpha=0):
        '''
        __init__ es un método especial que se usa para inicializar las
        instancias de una clase.

        Ej. de uso:
        >> mercurio = Planeta([x0, y0, vx0, vy0])
        >> print(mercurio.alpha)
        >> 0.
        '''
        self.y_actual = condicion_inicial
        self.t_actual = 0.
        self.alpha = alpha

    def ecuacion_de_movimiento(self):
        '''
        Implementa la ecuación de movimiento, como sistema de ecuaciónes de
        primer orden.
        '''
        x, y, vx, vy = self.y_actual
        r= (x**2 + y**2)**0.5
        G=1
        M=1
        m=1
        fx = -G*m*M*(1/r**2 - 2*self.alpha/r**3)*(x / r)
        fy = -G*m*M*(1/r**2 - 2*self.alpha/r**3)*(y/ r)
        return [vx, vy, fx, fy]

    def avanza_euler(self, dt):
        '''
        Toma la condición actual del planeta y avanza su posicion y velocidad
        en un intervalo de tiempo dt usando el método de Euler explícito. El
        método no retorna nada, pero re-setea los valores de self.y_actual.
        '''
        vx,vy,fx,fy=self.ecuacion_de_movimiento()
        x1=vx + dt*self.y_actual[0]
        y1=vy + dt*self.y_actual[1]
        vx1=fx + dt*self.y_actual[2]
        vy1=fy + dt*self.y_actual[3]
        self.y_actual=[x1,y1,vx1,vy1]
        self.t_actual+=dt
        pass

    def avanza_rk4(self, dt):
        '''
        Similar a avanza_euler, pero usando Runge-Kutta 4.
        '''
        yn = self.y_actual

        k1=self.ecuacion_de_movimiento()
        self.y_actual= yactual + dt*k1/2.

        k2=self.ecuacion_de_movimiento()
        self.y_actual= yactual + dt*k2/2

        k3=self.ecuacion_de_movimiento()
        self.y_actual= yactual + dt*k3/2

        k4=self.ecuacion_de_movimiento()

        '''x1 = x + (k1[0]/6. + k2[0]/3. + k3[0]/3. + k4[0]/6.)*dt
        y1 = y + (k1[1]/6. + k2[1]/3. + k3[1]/3. + k4[1]/6.)*dt
        vx1 = vx + (k1[2]/6. + k2[2]/3. + k3[2]/3. + k4[2]/6.)*dt
        vy1 = vy + (k1[3]/6. + k2[3]/3. + k3[3]/3. + k4[3]/6.)*dt'''


        self.y_actual = yn + (k1/6. + k2/3. + k3/3. + k4/6.)*dt
        self.t_actual + = dt
        pass

    def avanza_verlet(self, dt):
        '''
        Similar a avanza_euler, pero usando Verlet.
        '''
        x0, y0, vx0, vy0 = self.y_actual()
        ec_mov_n=self.ecuacion_de_movimiento()

        x1=x0+ dt*vx0 +ec_mov_n[2]*(dt**2)/2.
        y1=y0+ dt*vy0 +ec_mov_n[3]*(dt**2)/2.

        self.y_actual=[x1,y1,vx0,vy0]
        vx1,vy1,fx1,fy1= self.ecuacion_de_movimiento()
        vx1= vx0 + fx1*dt/2. + ec_mov_n[2]*(dt**2)/2.
        vy1= vy0 + fy1*dt/2. + ec_mov_n[3]*(dt**2)/2.

        self.y_actual=x1,y1,vx1,vy1]
        self.t_actual+=dt
        pass

    def energia_total(self):
        '''
        Calcula la enérgía total del sistema en las condiciones actuales.
        '''
        y = self.y_actual()
        ec= self.ecuacion_de_movimiento()
        r= (x**2 + y**2)**0.5
        self.energia_actual=0.5*m*(ec[0]**2 + ec[1]**2) + G*m*M(self.alpha/r**2 - 1/r)
        pass
