#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
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
        x0, y0, vx0, vy0= self.y_actual


    def ecuacion_de_movimiento(self):
        '''
        Implementa la ecuación de movimiento, como sistema de ecuaciónes de
        primer orden.
        '''
        x, y, vx, vy = self.y_actual
        r= (x**2 + y**2)**0.5
        fx = -(1/r**2 - 2*self.alpha/r**3)*(x / r)
        fy = -(1/r**2 - 2*self.alpha/r**3)*(y/ r)
        return np.array([vx, vy, fx, fy])

    def avanza_euler(self, dt):
        '''
        Toma la condición actual del planeta y avanza su posicion y velocidad
        en un intervalo de tiempo dt usando el método de Euler explícito. El
        método no retorna nada, pero re-setea los valores de self.y_actual.
        '''

        x= self.y_actual[0]
        y= self.y_actual[1]
        vx= self.y_actual[2]
        vy= self.y_actual[3]
        vx, vy, fx, fy = self.ecuacion_de_movimiento()
        x1= vx*dt + x
        y1= vy*dt + y
        vx1= fx*dt + vx
        vy1= fy*dt + vy
        self.y_actual =[x1,y1,vx1,vy1]
        self.t_actual += dt
        pass

    def avanza_rk4(self, dt):
        '''
        Similar a avanza_euler, pero usando Runge-Kutta 4.
        '''
        yn = self.y_actual

        k1= self.ecuacion_de_movimiento()
        self.y_actual= yn+dt*(k1/2.)

        k2= self.ecuacion_de_movimiento()
        self.y_actual= yn+dt*(k2/2.)


        k3= self.ecuacion_de_movimiento()
        self.y_actual= yn+dt*k3

        k4= self.ecuacion_de_movimiento()
        #self.y_anterior = yn

        self.y_actual = yn + (k1/6. + k2/3. + k3/3. + k4/6.)*dt
        self.t_actual += dt
        pass

    def avanza_verlet(self, dt):

        '''Similar a avanza_euler, pero usando Verlet.'''

        x0, y0, vx0, vy0 = self.y_actual
        fx = self.ecuacion_de_movimiento()[2]
        fy = self.ecuacion_de_movimiento()[3]

        xn_1 = x0 + dt*vx0 + fx*(dt**2)*0.5
        yn_1 = y0 + dt*vy0 + fy*(dt**2)*0.5

        self.y_actual=[xn_1,yn_1,vx0,vy0]
        fx1=self.ecuacion_de_movimiento()[2]
        fy1=self.ecuacion_de_movimiento()[3]


        vxn_1 = vx0 + (fx1 + fx)*dt*0.5
        vyn_1 = vy0 + (fy1 + fy)*dt*0.5

        self.y_actual = [xn_1, yn_1,  vxn_1, vyn_1]
        self.t_actual+=dt
        pass

    def energia_total(self):

        '''Calcula la energia total de el sistema en las condiciones actuales.'''

        x,y,vx,vy = self.y_actual
        #ec= self.ecuacion_de_movimiento()
        r = (x**2 + y**2)**0.5
        energia=0.5*(x**2 + y**2) + (self.alpha/r**2 - 1/r)
        return energia
        pass
