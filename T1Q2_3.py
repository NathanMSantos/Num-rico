import matplotlib.pyplot as plt
import math
import numpy

def dv_x(x_i, y_i):
    return 1.2*x_i - 0.6*x_i*y_i

def dv_y(x_i, y_i):
    return -0.8*y_i + 0.3*x_i*y_i

 
a = 0
b = 2
x0 = 2
y0 = 1
m  = 12

erro_x  = []
erro_y  = []
q_x     = []
q_y     = []
h       = []
dominio_t = []
#p_x     = []
#p_y     = []
p_norma = []
k       = 0
l       = 0


matriz_xn = []
matriz_yn = []
matriz_t  = []

x_i = x0
y_i = y0

x_aprox = []
y_aprox = []

eta_x = []
eta_y = []
p_x = []
p_y = []
p_x_norma = []
p_y_norma = []
k

for j in range(0 , m+1):
    N = int(math.pow(2, j+2))
    h.append( (b - a) / N)
    x_i=x0
    y_i = y0

    x_aprox.append(x0)
    y_aprox.append(y0)

    #print( "h N M", h, N, j)
    for i in range (0, N):
        t = a + i * h[j]
        dominio_t.append(t)
        w_x = x_i + h[j] * dv_x(x_i,y_i)
        x_aprox.append(w_x)

        w_y = y_i + h[j] * dv_y(x_i,y_i)
        y_i = w_y
        x_i = w_x
        y_aprox.append(w_y)

        if i == N-1:
            eta_x.append(w_x)
            eta_y.append(w_y)

    if j >= 2:
        p_x.append(abs((eta_x[j-2] - eta_x[j-1]) / (eta_x[j-1] - eta_x[j] )))
        p_y.append(abs((eta_y[j-2] - eta_y[j-1]) / (eta_y[j-1] - eta_y[j] )))
        p_x_norma.append(math.log2(abs((eta_x[j-2] - eta_x[j-1]) / (eta_x[j-1] - eta_x[j] ))))
        p_y_norma.append(math.log2(abs((eta_y[j-2] - eta_y[j-1]) / (eta_y[j-1] - eta_y[j] ))))
        #print(N, math.log2(p_x), math.log2(p_y))
        p_norma.append(numpy.log2( math.sqrt(math.pow(p_x[k],2) + math.pow(p_y[k], 2)) ))
        print(N, p_norma[k])
        k+=1

    dominio_t.append(b)        
    matriz_xn.append(x_aprox)
    matriz_yn.append(y_aprox)
    matriz_t.append(dominio_t)

    x_aprox = []
    y_aprox = []
    dominio_t = []


l = j = 0

""" #plt.plot (matriz_t[12],matriz_xn[12], color = "#000000", linestyle = "-", label = "Curva x numérica " + f"{12}")
plt.plot (matriz_t[12],matriz_xn[12], color = "#000000", linestyle = "-", label = "Presa ")
# plt.plot (matriz_t[5],matriz_xn[5], color = "#000000", linestyle = "-", label = "Presa ")


#plt.plot (matriz_t[12],matriz_yn[12], color = "#000000", linestyle = ":", label = "Curva y numérica " + f"{12}")
plt.plot (matriz_t[12],matriz_yn[12], color = "#000000", linestyle = "-.", label = "Predador")
# plt.plot (matriz_t[5],matriz_yn[5], color = "#000000", linestyle = "-.", label = "Predador")


plt.ylabel("Espécie competindo")
plt.xlabel("Tempo")
plt.title("Presa x Predador")
plt.legend()
plt.show()
 """

with open("behavior_convergence_Q2_3.txt", 'w', encoding='utf-8') as file2:
        file2.write("ORDER BEHAVIOR CONVERGENCE TABLE\n");
        j=l=0
        for i in range (0, m+1):
            if i<=1:
                #print(" %5d  %9.3e  %9.3e \n" % (math.pow(2, i+2),h, erro[i]));
                file2.write("{:5d} & {:9.3e}\\\\\n".format(int(math.pow(2, i+2)),h[j]))   
            else:
                #print(" %5d  %9.3e  %9.3e  %9.3e \n" % (math.pow(2, i+2),h, erro[i], q[l]));
                file2.write("{:5d} & {:9.3e} & {:9.3e} & {:9.3e} & {:9.3e}\\\\\n".format(int(math.pow(2, i+2)),h[j],p_x_norma[l],p_y_norma[l], p_norma[l]))  
                l+=1
            j+=1
 