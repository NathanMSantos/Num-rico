import math

def y(t):
    x = (-100*t)
    return(math.pow(math.e,-100*t))

def dv_f(y_i):
    return (-100*y_i)


"""def y(t):
   return((math.sin(2*t*math.pi))*(math.pow(math.e,-0.2*t)))

def dv_f(y_i, t):
    return (-0.2*y_i+2*math.pi*(math.cos(2*t*math.pi))*(math.pow(math.e,-0.2*t)))"""

a = 0
b = 0.25
N = 8192
y0 = 1
x0 = 0
    
h = (b - a)/N
y_i = y0

for i in range (0,N):
    t = a + i * h
    w = y_i + h * dv_f(y_i)
    #w = y_i + h * dv_f(y_i, t)
    #print ("i = " + f"{i}" + "     t = " + f"{t}" + "       y = " + f"{y_i:.1E}" + "        f(x,y) = y' = " + f"{dv_f(y_i):.1E}" + "       yk+1 = " + f"{w:.1E}")
    #print ("i = " + f"{i}" + "     t = " + f"{t}" + "       y = " + f"{y_i:.1E}" + "        f(x,y) = y' = " + f"{dv_f(y_i,t):.1E}" + "       yk+1 = " + f"{w:.1E}")
    y_i = w

t += h
print (t)
ex = y(t)
erro = ex - w

print("\nyexato =" + f"{ex:.1E}" + "    ynum =   " + f"{w:.1E}" ); 
print("n = %5d      h = %9.3e   erro = %9.3e \n" % (N,h, erro)); 
  