import matplotlib.pyplot as plt
import math

def y(t):
    return (70/9) * math.pow(math.e, -0.3*t) - (43/9) * math.pow(math.e, -1.2*t)

def dv_f(t, y_i):
    return -1.2*y_i + 7*math.pow(math.e, -0.3*t)

a = 0
b = 2.5
y0 = 3
m = 12

dominio_t = []
imagem_yn = []
matriz_yn = []
matriz_t = []
imagem_ye = []
erro = []
p = []
h = []
k = 0
l = 1

y_i = y0

for j in range(0 , m+1):
    N = int(math.pow(2, j+2))                       #cria os N's de acordo com o valor de m 
    h.append( (b - a) / N)
    y_i = y0
    imagem_yn = []
    dominio_t = []
    imagem_yn.insert(0, y0)
    for i in range (0, N):
        t = a + i * h[j]
        dominio_t.append(t)
        w = y_i + h[j]* dv_f(t,y_i)                #aplica o método de euler chamando a função da derivada
        imagem_yn.append(w)  
        y_i = w
        if i == N-1:
            t+=h[j]
            erro.append(abs(y(t) - y_i))          #calcula e armazena o erro em um vetor
            k+=1
    dominio_t.append(b)
    matriz_yn.append(imagem_yn)
    matriz_t.append(dominio_t)
    if j > 0:
        p.append(math.log(abs(erro[l-1]/erro[l]),10)/math.log((h[l-1]/h[l]),10))    #calcula e armazena o p
        l+=1


#discretização do dominio

t=a
while (t<=b):
    imagem_ye.insert(i, y(t))        
    t += h[j]
    i += 1


#construção da tabela de convergencia

l = j = 0

with open("behavior_convergence_Q2_1.txt", 'w', encoding='utf-8') as file2:
        file2.write("ORDER BEHAVIOR CONVERGENCE TABLE\n");
        for i in range (0, m+1):
            if i<1:
                #print(" %5d  %9.3e  %9.3e \n" % (math.pow(2, i+2),h, erro[i]));
                file2.write("{:5d} & {:9.3e} & {:9.3e}\\\\\n".format(int(math.pow(2, i+2)),h[j],erro[i]))   
            else:
                #print(" %5d  %9.3e  %9.3e  %9.3e \n" % (math.pow(2, i+2),h, erro[i], q[l]));
                file2.write("{:5d} & {:9.3e} & {:9.3e} & {:9.3e}\\\\\n".format(int(math.pow(2, i+2)),h[j],erro[i],p[l]))  
                l+=1
            j+=1


#plotagem do gráfico

plt.plot (dominio_t,imagem_ye, color = "#000000", label = "Curva x exata")
for j in range(0 , m+1):
  if j == 6 or j == 9 or j == 12:  
    plt.plot (matriz_t[j],matriz_yn[j], color = "#000000", linestyle = "--", label = "Curva x numérica " + f"{j}")
plt.ylabel("Eixo x")
plt.xlabel("Eixo t")
plt.title("Gráfico de [y=....] em função do tempo")
plt.legend()
plt.show()