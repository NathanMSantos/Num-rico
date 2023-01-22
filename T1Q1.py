import matplotlib.pyplot as plt
import math

pi = math.pi
graficos = [1,2,3]
dominio_x = []
x=0
i=1

while (x<=2*pi):
    dominio_x.insert(i, x-pi)        
    x += 0.05
    i += 1

for m in graficos:
    for t in dominio_x:
        y = [math.cos(m*t) for t in dominio_x]     
    plt.xticks([-pi,0,pi])
    plt.yticks([-1,0,1])
    if (m==1):
        plt.plot (dominio_x,y, color = "#000000", label = "Curva m = 1")
    if (m==2):
        plt.plot (dominio_x,y, color = "#000000", linestyle = "--", label = "Curva m = 2")
    if (m==3):
        plt.plot (dominio_x,y, color = "#000000", linestyle = ":", label = "Curva m = 3")

plt.ylabel("Eixo y")
plt.xlabel("Eixo t")
plt.title("Gráfico de [y=cos(mt)] em função do tempo")
plt.legend()
plt.show()