import matplotlib.pyplot as plt
import math

#declarações
imagem_xe = []
imagem_ye = []
imagem_xn = []
imagem_yn = []
dominio_t = []
matriz_xn = []
matriz_yn = []
matriz_t = []
vetorerro_x = []
vetorerro_y = []
vetornorma_max = []

#funções trabalhadas e suas derivadas
def x(t):
    return((math.pow(math.e,-t))*((math.cos(t))-3*math.sin(t)))

def y(t):
    return((math.pow(math.e,-t))*((math.cos(t))-math.sin(t)))

def dv_fx(x_i,y_i):
    return (x_i-5*y_i)

def dv_fy(x_i, y_i):
    return (x_i-3*y_i)


#intervalos de trabalho, m, h e valores iniciais p as variaveis 
a = 0
b = 2
m = 12
h = []
t01 = 0
x01 = 1
y01 = 1
l = 0

for j in range(0 , m+1):
    N = int(math.pow(2, j+2))
    h.append( (b - a) / N)
    
    x_i = x01      
    y_i = y01
    imagem_xn = []
    imagem_yn = []
    dominio_t = []
    imagem_xn.insert(0, x01) 
    imagem_yn.insert(0, y01)

    for i in range (0,N):
        t = a + i * h[j]
        dominio_t.append(t)
        w = x_i + h[j]* dv_fx(x_i, y_i)
        imagem_xn.append(w)
        z = y_i + h[j]* dv_fy(x_i, y_i)
        imagem_yn.append(z)  
        x_i = w
        y_i = z
    
    dominio_t.append(b)
    erro_x = x(b) - w
    erro_y = y(b) - z

    matriz_xn.append(imagem_xn)
    matriz_yn.append(imagem_yn)
    matriz_t.append(dominio_t)
    vetorerro_x.append(erro_x) 
    vetorerro_y.append(erro_y)
    vetornorma_max.append(math.sqrt(math.pow(erro_x,2)+math.pow(erro_y,2)))

print(vetornorma_max)
t=a
while (t<=b):
    imagem_xe.insert(i, x(t)) 
    imagem_ye.insert(i, y(t))        
    t += h[j]
    i += 1

"""
for j in range(0 , m+1):
    print (matriz_t[j])
    print ("t\nx")
    print (matriz_xn[j])
    print ("x\ny")
    print (matriz_yn[j])
    print ("\n")

print (imagem_xe)
print ("xe\nye")
print (imagem_ye)"""

plt.plot (dominio_t,imagem_xe, color = "#000000", label = "Curva x exata")
for j in range(0 , m+1):
  if j == 6 or j == 9 or j == 12:  
    plt.plot (matriz_t[j],matriz_xn[j], color = "#000000", linestyle = "--", label = "Curva x numérica " + f"{j}")
plt.ylabel("Eixo x")
plt.xlabel("Eixo t")
plt.title("Gráfico de [x=....] em função do tempo")
plt.legend()
plt.show()

plt.plot (dominio_t,imagem_ye, color = "#000000", label = "Curva y exata")
for j in range(0 , m+1):
   if j == 6 or j == 9 or j == 12:   
    plt.plot (matriz_t[j],matriz_yn[j], color = "#000000", linestyle = "--", label = "Curva y numérica " + f"{j}")
plt.ylabel("Eixo y")
plt.xlabel("Eixo t")
plt.title("Gráfico de [y=...] em função do tempo")
plt.legend()
plt.show()



