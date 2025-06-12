def x(n):
    if n%2==0:
        return n**2-1
    else:
        return (n**2-1)/2

def y(n):
    if n%2==0:
        return 2*n
    else:
        return n
def z(x, y):
    return (x**2+y**2)**0.5

def tabla_ternas(n):
    i = 1
    while i <= n:
        a = x(i)
        b = y(i)
        c = z(a, b)
        print(f"{i} ({a}, {b}, {c})")
        i+=1
        
tabla_ternas(10)
