from math import *
import numpy as np
import matplotlib.pyplot as plt
import math


###################################
# parametros iniciais
###################################


t0 = 0.0                    # instante inicial
tf = 5.0                    # instante final
n_lista = [4, 8, 16, 32, 64, 128, \
          256, 512, 1024, 2048]     # qtd de ptos a cada execucao
y0 = np.array([1, 1])


###################################
#funções trabalhadas e suas derivadas
###################################

def f(y,t):                 # f tq dy/dt = f(y,t)

    return np.array( [ y[0]-5*y[1], \
                       y[0]-3*y[1] ])

def solucao(t):             # expressao analitica para y(t)

    return np.array( [((math.pow(math.e,-t))*((math.cos(t))-3*math.sin(t))), \
                      ((math.pow(math.e,-t))*((math.cos(t))-math.sin(t)))] )

###################################
# executar o metodo do trapézio e MAS
###################################


h_lista = []
t_lista = []
y_lista = []
erro_lista = []
q = []
valor_aprox = []
j=0

valor_aprox.append(y0)


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
################################################################################        


    # adiciona nos dados para o grafico e a tabela
    valor_aprox.append(y[i+1]) #valor aproximado em um memso tempo T
    
    t_lista.append(t)
    y_lista.append(y)
    h_lista.append(h)
    erro_lista.append( np.linalg.norm(y[n] - solucao(tf)) )
    
    
    # Cálculo da ordem de convergência e do erro
    if j >= 2:
        valor_absoluto = abs(np.linalg.norm((valor_aprox[j-2]) - valor_aprox[j-1])/np.linalg.norm(valor_aprox[j-1] - valor_aprox[j]))
        q.append(np.log2(valor_absoluto))
    j+=1

# exibe o grafico com as curvas de y[0]

for w in range(len(n_lista)):
    t = t_lista[w]
    y = y_lista[w]
    
    plt.plot(t, y[:,0], label="n=%d"%n_lista[w], color = "#000000")

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
    
    plt.plot(t, y[:,1], label="n=%d"%n_lista[w], color = "#000000")

plt.title('aprox para a 2a coordenada')
plt.xlabel('t[i]')
plt.ylabel('y[1][i]')
plt.grid(True)
plt.legend()
plt.show()

# faz a curva em 2d

for w in range(len(n_lista)):
    y = y_lista[w]
    
    plt.plot(y[:,0], y[:,1], label="n=%d"%n_lista[w], color = "#000000")

plt.title('aprox para a curva em 2d')
plt.xlabel('y[0][i]')
plt.ylabel('y[1][i]')
plt.grid(True)
plt.legend()
plt.show()


# exibe o grafico com o erro

plt.title('decaimento do erro no instante final')
plt.xlabel('h')
plt.ylabel('erro(h, %1.2f)'%tf)
plt.grid(True)
plt.plot(h_lista, erro_lista, color = "#000000")
plt.show()

# escreve a tabela

print()
print("n", "h", "erro(h, %1.2f)"%tf, sep='\t')
for w in range(len(n_lista)):
    print(n_lista[w], h_lista[w], erro_lista[w], sep='\t')


# cria arquivo com tabela formatada
with open("behavior_convergence_T3_Q1_teste.txt", 'w', encoding='utf-8') as file2:
        file2.write("ORDER BEHAVIOR CONVERGENCE TABLE\n");
        j=l=0
        for i in range (len(n_lista)):
            if i<1:
                file2.write("{:5d} & {:9.3e} & {:9.3e}\\\\\n".format(n_lista[j], h_lista[j], erro_lista[j]))   
            else:
                #file2.write("{:5d} & {:9.3e} & {:9.3e} & {:9.3e}\\\\\n".format(n_lista[j],h_lista[j],erro_lista[j]))  
                file2.write("{:5d} & {:9.3e} & {:9.3e} & {:9.3e}\\\\\n".format(n_lista[j],h_lista[j],erro_lista[j],q[l]))  
                l+=1
            j+=1