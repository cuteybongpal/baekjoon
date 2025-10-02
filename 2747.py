a = int(input())

fibonacci =[0] * 1000
fibonacci[1] = 1
def fibo(n):
    if n <= 1:
        return
    if fibonacci[n-1] == 0:
        fibo(n-1)
    if fibonacci[n-2] == 0:
        fibo(n-2)
    fibonacci[n] = fibonacci[n-1] + fibonacci[n-2]
fibo(a)
print(fibonacci[a])