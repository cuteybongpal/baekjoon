def move(n, x, y):
    if n > 1:
        move(n-1, x, 6 - x - y)
    print(x, y)

    if n > 1:
        move(n-1, 6-x-y, y)
    
a = int(input())
print(2**a-1)
if a <= 20:
    move(a, 1, 3)