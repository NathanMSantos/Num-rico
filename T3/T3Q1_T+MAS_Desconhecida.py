from math import *
import numpy as np
import matplotlib.pyplot as plt
import math

# parametros iniciais

t0 = 0.0   # instante inicial
tf = 5.0   # instante final
m = 12    # qtd de ptos a cada execucao
n_lista = []
for i in range (1, m+1):
    n_lista.append(int(math.pow(2, i+2)))
y0 = np.array([2, 1])


#funções trabalhadas e suas derivadas

def f(y,t):                 # f tq dy/dt = f(y,t)
    return np.array( [ 1.2*y[0] - 0.6*y[0]*y[1], \
                       -0.8*y[1] + 0.3*y[0]*y[1] ])

# executar o metodo do trapézio e MAS

h_lista = []
t_lista = []
y_lista = []
q = []
erro_lista = []
valor_aprox = []
j=0
k=0

valor_aprox.append(y0)

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
        ytil = y[i] + h*f(y[i], t[i])
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
    valor_aprox.append(y[i+1]) #valor aproximado em um memso tempo T
    
    t_lista.append(t)
    y_lista.append(y)
    h_lista.append(h)

    # Cálculo da ordem de convergência e do erro
    if j >= 2:
        valor_absoluto = abs(np.linalg.norm((valor_aprox[j-2]) - valor_aprox[j-1])/np.linalg.norm(valor_aprox[j-1] - valor_aprox[j]))
        q.append(np.log2(valor_absoluto))

        erro_lista.append((abs(np.linalg.norm(valor_aprox[j-1] - valor_aprox[j]) / (math.pow(2, q[k]) - 1))))
        print(erro_lista)
        k+=1
    j+=1

# exibe o grafico com as curvas de y[0]

for w in range(len(n_lista)):
    t = t_lista[w]
    y = y_lista[w]
    
    plt.plot(t, y[:,0], label="n=%d"%n_lista[w])

plt.title('aprox para a 1a coordenada')
plt.xlabel('t[i]')
plt.ylabel('y[0][i]')
plt.grid(True)
plt.legend()
plt.show()

# exibe o grafico com as curvas de y[1]

for w in range(len(n_lista)):
    t = t_lista[w]
    y = y_lista[w]
    
    plt.plot(t, y[:,1], label="n=%d"%n_lista[w])

plt.title('aprox para a 2a coordenada')
plt.xlabel('t[i]')
plt.ylabel('y[1][i]')
plt.grid(True)
plt.legend()
plt.show()

# faz a curva em 2d

for w in range(len(n_lista)):
    y = y_lista[w]
    
    plt.plot(y[:,0], y[:,1], label="n=%d"%n_lista[w])

plt.title('aprox para a curva em 2d')
plt.xlabel('y[0][i]')
plt.ylabel('y[1][i]')
plt.grid(True)
plt.legend()
plt.show()

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