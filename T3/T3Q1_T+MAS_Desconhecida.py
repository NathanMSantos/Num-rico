from math import *
import numpy as np
import matplotlib.pyplot as plt
import math

# parametros iniciais

t0 = 0.0   # instante inicial
tf = 5.0   # instante final
n_lista = [4, 8, 16, 32, 64, 128, \
          256, 512, 1024, 2048]     # qtd de ptos a cada execucao

y0 = np.array([2, 1])

#funções trabalhadas e suas derivadas

def f(y,t):                 # f tq dy/dt = f(y,t)
    return np.array( [ 1.2*y[0] - 0.6*y[0]*y[1], \
                       -0.8*y[1] + 0.3*y[0]*y[1] ])

# executar o metodo do trapézio e MAS

h_lista = []
t_lista = []
y_lista = []
erro_lista = []
norma = []
j=0

for n in n_lista:
    
    h = (tf-t0)/float(n)

    # executa o metodo
    y = np.zeros([n+1, 2])
    t = np.zeros(n+1)

    t[0] = t0
    y[0] = y0

    for i in range(0,n):
        t[i+1] = t0 + (i+1)*h

        # chute inicial
        ytil = y[i] + h*(1/2)*(f(y[i],t[i]) + f(y[i],t[i]))
        alteracao = 1.0
        
        # iteracoes de pto fixo
        r = 0
        while r<20 and alteracao > 0.0001:
            ytil0 = ytil
            ytil = y[i] + h*(1/2)*(f(y[i],t[i]) + f(ytil,t[i+1]))
            alteracao = np.linalg.norm(ytil-ytil0)
            r = r + 1
        
        y[i+1] = ytil
    # adiciona nos dados para o grafico e a tabela
    
    #cálculo da norma
    # norma.append(np.linalg.norm(y[i]))
    norma.append(y[i])
    
    t_lista.append(t)
    y_lista.append(y)
    h_lista.append(h)

    # Cálculo do erro
    if j >= 2:
        erro_lista.append((norma[j-2] - norma[j-1])/(norma[j-1] - norma[j]))
        print(np.log2(erro_lista))
    j+=1

# exibe o grafico com as curvas de y[0]

# for w in range(len(n_lista)):
#     t = t_lista[w]
#     y = y_lista[w]
    
#     plt.plot(t, y[:,0], label="n=%d"%n_lista[w])

# plt.title('aprox para a 1a coordenada')
# plt.xlabel('t[i]')
# plt.ylabel('y[0][i]')
# plt.grid(True)
# plt.legend()
# plt.show()

# # exibe o grafico com as curvas de y[1]

# for w in range(len(n_lista)):
#     t = t_lista[w]
#     y = y_lista[w]
    
#     plt.plot(t, y[:,1], label="n=%d"%n_lista[w])

# plt.title('aprox para a 2a coordenada')
# plt.xlabel('t[i]')
# plt.ylabel('y[1][i]')
# plt.grid(True)
# plt.legend()
# plt.show()

# # faz a curva em 2d

# for w in range(len(n_lista)):
#     y = y_lista[w]
    
#     plt.plot(y[:,0], y[:,1], label="n=%d"%n_lista[w])

# plt.title('aprox para a curva em 2d')
# plt.xlabel('y[0][i]')
# plt.ylabel('y[1][i]')
# plt.grid(True)
# plt.legend()
# plt.show()

# exibe o grafico com o erro

""" plt.title('decaimento do erro no instante final')
plt.xlabel('h')
plt.ylabel('erro(h, %1.2f)'%tf)
plt.grid(True)
plt.plot(h_lista,erro_lista)
plt.show()

# escreve a tabela

print()
print("n", "h", "erro(h, %1.2f)"%tf, sep='\t')
for w in range(len(n_lista)):
    print(n_lista[w], h_lista[w], erro_lista[w], sep='\t')"""