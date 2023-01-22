import matplotlib.pyplot as plt
import math

imagem_xe = []
imagem_ye = []
imagem_xn = []
imagem_yn = []
dominio_t = []

def x(t):
    return((math.pow(math.e,-t))*((math.cos(t))-3*math.sin(t)))

def y(t):
    return((math.pow(math.e,-t))*((math.cos(t))-math.sin(t)))

def dv_fx(x_i,y_i):
    return (x_i-5*y_i)

def dv_fy(x_i, y_i):
    return (x_i-3*y_i)

a = 0
b = 10
N = 1000000
x01 = 0
y01 = 1
x02 = 0
y02 = 1
    
h = (b - a)/N

y_i = y01
x_i = x01

imagem_xn.insert(0, x01) 
imagem_yn.insert(0, y02)

for i in range (0,N):
    w = x_i + h * dv_fx(x_i, y_i)
    imagem_xn.append(w)
    z = y_i + h * dv_fy(x_i, y_i)
    imagem_yn.append(z)
    #print ("i = " + f"{i}" + "     t = " + f"{t}" + "       y = " + f"{y_i:.1E}" + "        f(x,y) = y' = " + f"{dv_f(y_i,t):.1E}" + "       yk+1 = " + f"{w:.1E}")   
    x_i = w
    y_i = z

ex_x = x(b)
ex_y = y(b)
erro_x = ex_x - w
erro_y = ex_y - z

print("\nyexat_x =" + f"{ex_x:.1E}" + "    ynum_x =   " + f"{w:.1E}" )
print("yexat_y =" + f"{ex_y:.1E}" + "    ynum_y =   " + f"{z:.1E}" ) 
print("\nn = %9.3e      h = %9.3e   erro_x = %9.3e    erro_y = %9.3e  \n" % (N,h, erro_x, erro_y)) 

t=0
i=1

while (t<=b):
    dominio_t.insert(i, t)
    imagem_xe.insert(i, x(t)) 
    imagem_ye.insert(i, y(t))        
    t += h
    i += 1

plt.plot (dominio_t,imagem_xe, color = "#000000", label = "Curva x exata")
plt.plot (dominio_t,imagem_xn, color = "#000000", linestyle = "--", label = "Curva x numérica")
plt.ylabel("Eixo x")
plt.xlabel("Eixo t")
plt.title("Gráfico de [x=....] em função do tempo")
plt.legend(bbox_to_anchor = (1.3,0.7))
plt.show()

plt.plot (dominio_t,imagem_ye, color = "#000000", label = "Curva y exata")
plt.plot (dominio_t,imagem_yn, color = "#000000", linestyle = "--", label = "Curva y numérica")
plt.ylabel("Eixo y")
plt.xlabel("Eixo t")
plt.title("Gráfico de [y=...] em função do tempo")
plt.legend(bbox_to_anchor = (1.3,0.7))
plt.show()



"""
u_i = 3
dv1u_i = -4

def f(t, u_i, dv1u_i):
    t = a + i * h
    #uma genérica, tem que pedir o usuário para digitar a equação
    #print("t e w(em f):", t, w)
    return (-(dv1u_i*dv1u_i*u_i)+(t*t*u_i*u_i))

b, N = input("Digite os valor b do intervalo [2,b] e o número de divisões N:").split()

a = u_i
b = float(b)
N = int(N)

h = (b - a)/N
t = a
 
print ("h, t e u(2): ", h, t, u_i)

for i in range (1, N+1):
    u = u_i + h * dv1u_i
    t = a + i * h
    print("%5d & %9.3e  \\\\" % (i,u))

t = a
for i in range (1, N+1):
    dv2u_i = dv1u_i + h * f(t, u_i, dv1u_i)
    t = a + i * h
    print("%5d & %9.3e  \\\\" % (i,dv2u_i)); 
"""