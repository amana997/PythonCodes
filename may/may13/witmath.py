import sympy

for _ in range(int(input())):
    n = int(input())
    while (not sympy.isprime(n)):
        n -= 1 
    print(n)
