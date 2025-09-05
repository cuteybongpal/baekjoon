a = int(input())
b = int(input())
c = int(input())


res = a*b*c

dict = [0,0,0,0,0,0,0,0,0,0]
for i in str(res):
    for j in range(0,10):
        if j == int(i):
            dict[j] += 1


for i in range(0, 10):
    print(dict[i])