a = int(input())

list = map(int, input().split())

count = 0
for i in list:
    isPrime = True;
    if i == 1 or i == 0:
        isPrime = False
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
    if isPrime:
        count += 1

print(count)