import matplotlib.pyplot as plt
import math
import numpy

""" def y(t):
    return (70/9) * math.pow(math.e, -0.3*t) - (43/9) * math.pow(math.e, -1.2*t)
 """

def dv_x(x_i, y_i):
    return 1.2*x_i - 0.6*x_i*y_i

def dv_y(x_i, y_i):
    return -0.8*y_i + 0.3*x_i*y_i

 
a = 0
b = 20
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
            p_x = (numpy.log2(abs((x_aprox[i-3] - x_aprox[i-2]) / (x_aprox[i-2] - x_aprox[i-1] ))))
            p_y = (numpy.log2(abs((y_aprox[i-3] - y_aprox[i-2]) / (y_aprox[i-2] - y_aprox[i-1] ))))
            #print(N, p_x, p_y)
            #p_norma.append(numpy.log2( math.sqrt( math.pow(p_x,2) + math.pow(p_y, 2)) ))
            #print (N, p_norma[j])
    dominio_t.append(b)        
    matriz_xn.append(x_aprox)
    matriz_yn.append(y_aprox)
    matriz_t.append(dominio_t)

    x_aprox = []
    y_aprox = []
    dominio_t = []


l = j = 0

""" for j in range(0 , m+1):
    print (matriz_t[j])
    print ("t\nx")
    print (matriz_xn[j])
    print ("x\ny")
    print (matriz_yn[j])
    print ("\n") 

 """


#plt.plot (matriz_t[12],matriz_xn[12], color = "#000000", linestyle = "-", label = "Curva x numérica " + f"{12}")
plt.plot (matriz_t[6],matriz_xn[6], color = "#000000", linestyle = "-", label = "Presa ")

#plt.plot (matriz_t[12],matriz_yn[12], color = "#000000", linestyle = ":", label = "Curva y numérica " + f"{12}")
plt.plot (matriz_t[6],matriz_yn[6], color = "#000000", linestyle = "-.", label = "Predador")

plt.ylabel("Espécie competindo")
plt.xlabel("Tempo")
plt.title("Presa x Predador")
plt.legend()
plt.show()

 

""" with open("behavior_convergence.txt", 'w', encoding='utf-8') as file2:
        file2.write("ORDER BEHAVIOR CONVERGENCE TABLE\n");
        for i in range (0, m+1):
            if i<1:
                #print(" %5d  %9.3e  %9.3e \n" % (math.pow(2, i+2),h, erro[i]));
                file2.write("{:5d} & {:9.3e} & {:9.3e}\\\\\n".format(int(math.pow(2, i+2)),h[j],erro[i]))   
            else:
                #print(" %5d  %9.3e  %9.3e  %9.3e \n" % (math.pow(2, i+2),h, erro[i], q[l]));
                file2.write("{:5d} & {:9.3e} & {:9.3e} & {:9.3e}\\\\\n".format(int(math.pow(2, i+2)),h[j],erro[i],q[l]))  
                l+=1
            j+=1 """