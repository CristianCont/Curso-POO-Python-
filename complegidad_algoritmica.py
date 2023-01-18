import sys
import time

def factorial(n):
    respuesta=1

    while n >1 :
        respuesta*=n
        n -= 1
    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    return n * factorial_r(n - 1)

if __name__ == '__main__':

    sys.setrecursionlimit(5000)
   
    n=2000
    comienzo=time.time()
    factorial(n)
    final=time.time()
    print(final-comienzo)

    comienzo1=time.time()
    factorial_r(n)
    final1=time.time()
    print(final1-comienzo1)
    