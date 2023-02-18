from math import factorial

def choose(n,r):
    return factorial(n) // (factorial(r)*factorial(n-r))

def C(n):
    return choose(2*n,n)//(n+1)

