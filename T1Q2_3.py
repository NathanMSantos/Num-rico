
import math

""" def y(t):
    return (70/9) * math.pow(math.e, -0.3*t) - (43/9) * math.pow(math.e, -1.2*t)
 """

def dv_x(x_i, y_i):
    return 1.2*x_i - 0.6*x_i*y_i

def dv_y(x_i, y_i):
    return -0.8*y_i + 0.3*x_i*y_i

 
a = 0
b = 5
x0 = 2
y0 = 1
m = 12

erro_x = []
erro_y = []
q_x = []
q_y = []
h = []
k = 0
l = 0

x_i = x0
y_i = y0

x_aprox = []
y_aprox = []

x_aprox.append(x0)
y_aprox.append(y0)

for j in range(0 , m+1):
    N = int(math.pow(2, j+2))
    h.append( (b - a) / N)
    x_i=x0
    y_i = y0
    #print( "h N M", h, N, j)
    for i in range (0, N):
        t = a + i * h[j]

        w_x = x_i + h[j] * dv_x(x_i,y_i)
        x_i = w_x
        x_aprox.append(w_x)

        w_y = y_i + h[j] * dv_y(x_i,y_i)
        y_i = w_y
        y_aprox.append(w_y)

    if j > 0:
        
        #print (j, f"{erro[l]: .9E}", f"{erro[l+1]: .9E}", f"{q[l]: .5E}" )
        l+=1

l = j = 0



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