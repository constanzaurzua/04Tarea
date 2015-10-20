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
        c_actual= [x1,y1,vx1,vy1]
        self.y_actual=c_actual
        self.t_actual+=dt
        pass

    def avanza_rk4(self, dt):
        '''
        Similar a avanza_euler, pero usando Runge-Kutta 4.
        '''
        
        pass

    def avanza_verlet(self, dt):
        '''
        Similar a avanza_euler, pero usando Verlet.
        '''
        pass

    def energia_total(self):
        '''
        Calcula la enérgía total del sistema en las condiciones actuales.
        '''
        pass
