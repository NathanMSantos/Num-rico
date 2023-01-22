
def f(t , w):
    #uma genérica, tem que pedir o usuário para digitar a equação
    #print("t e w(em f):", t, w)
    return (w - t*t + 1)



a, b, N, y0 = input("Digite os valores do intervalo, N e y0:").split()

a = float(a)
b = float(b)
N = int(N)
y0 = float(y0)
    
h = (b - a)/N
t = a
w = y0

print ("h, t e w0: ", h, t, w)



for i in range (1, N+1):
    w = w + h * f(t, w)
    t = a + i * h

    print("%5d & %9.3e  \\\\" % (i,w)); 
    #print("i: w e t:",i, w, t)
