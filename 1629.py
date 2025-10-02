import sys
a, b, c = map(int, sys.stdin.readline().split())

def pow(a:int, b:int, c:int):
    if b == 1:
        return (a % c)
    
    if b % 2 == 0:
        return pow(a, b//2, c)**2 % c
    else:
        res = pow(a, b//2, c)
        return ((res**2) *(a % c))   % c

print(pow(a,b,c))