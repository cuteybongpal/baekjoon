a = int(input())
aaaa = []
numbers = []

for k in range(a):
    b = int(input())
    numbers.append(b)

pn = [True] * (max(numbers) + 1)
pn[0] = False
pn[1] = False

for i in range(2,int(max(numbers)**0.5) + 1):
    if pn[i] == False:
        continue

    for j in range(i*i, int(max(numbers)) + 1, i):
        pn[j] = False
        
for k in numbers:

    p = k // 2
    while p >= 2:
        if pn[p] and pn[k-p]:
            print(p, k - p)
            break;
        p -= 1