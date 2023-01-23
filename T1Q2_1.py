import math

def y(t):
    return (70/9) * math.pow(math.e, -0.3*t) - (43/9) * math.pow(math.e, -1.2*t)

def dv_f(t, y_i):
    return -1.2*y_i + 7*math.pow(math.e, -0.3*t)
 

""" def y(t):
    x = (-100*t)
    return(math.pow(math.e,-100*t))

def dv_f(y_i):
    return (-100*y_i)
 """

a = 0
b = 2.5
y0 = 3
""" x0 = 0 
a = 0
b = 0.25
y0=1 """
m = 12

erro = []
p = []
h = []
k = 0
l = 1

y_i = y0

for j in range(0 , m+1):
    N = int(math.pow(2, j+2))
    h.append( (b - a) / N)
    y_i = y0
    #print( "h N M", h, N, j)
    for i in range (0, N):
        t = a + i * h[j]
        w = y_i + h[j]* dv_f(t,y_i)
        y_i = w
        if i == N-1:
            t+=h[j]
            erro.append(abs(y(t) - y_i))
            #print (i+1, f"{erro[k]: .9E}")
            k+=1
    if j > 0:
        p.append(math.log(abs(erro[l-1]/erro[l]),10)/math.log((h[l-1]/h[l]),10))
        #print (j, f"{erro[l]: .9E}", f"{erro[l+1]: .9E}", f"{q[l]: .5E}" )
        l+=1

l = j = 0

with open("behavior_convergence.txt", 'w', encoding='utf-8') as file2:
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