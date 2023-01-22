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
