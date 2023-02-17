from math import *
import numpy as np
import matplotlib.pyplot as plt
import math


###################################
# parametros iniciais
###################################


t0 = 0.0                    # instante inicial
tf = 5.0                    # instante final
n_lista = [40, 80, 160]     # qtd de ptos a cada execucao
y0 = np.array([1, 1])


###################################
#funções trabalhadas e suas derivadas
###################################


def y1(t):
    return((math.pow(math.e,-t))*((math.cos(t))-3*math.sin(t)))

def y2(t):
    return((math.pow(math.e,-t))*((math.cos(t))-math.sin(t)))

def dv_fy1(y1_i,y2_i):
    return (y1_i-5*y2_i)

def dv_fy2(y1_i, y2_i):
    return (y1_i-3*y2_i)


###################################
# executar o metodo do trapézio e MAS
###################################


h_lista = []
t_lista = []
y_lista = []
erro_lista = []

for n in n_lista:
    
    h = (tf-t0)/float(n)

    # executa o metodo
    y = np.zeros([n+1, 2])
    t = np.zeros(n+1)

    t[0] = t0
    y[0] = y0


################################################################################
    for i in range(0,n):
        t[i+1] = t0 + (i+1)*h

        # chute inicial
        ytil = y[i] + h*f(y[i],t[i])
        alteracao = 1.0
        
        # iteracoes de pto fixo
        r = 0
        while r<20 and alteracao > 0.0001:
            ytil0 = ytil
            ytil = y[i] + h*f(ytil,t[i+1])
            alteracao = np.linalg.norm(ytil-ytil0)
            r = r + 1
            print (r, ytil, alteracao )
        
        
        y[i+1] = ytil
################################################################################