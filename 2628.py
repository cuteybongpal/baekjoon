x,y = map(int, input().split())

mmap = []
for i in range(y):
    for j in range(x):
        mmap.append((j,i))
a = int(input())

cuttedArea = [mmap]
list = []


for i in range(a):
    snum, sm = map(int, input().split())
    
    for j in cuttedArea:
        list1 = []
        list2 = []
        if snum == 0:
            for k in j:
                if (k[1] >= sm):
                    list1.append(k)
                else:
                    list2.append(k)
        elif snum == 1:
            for k in j:   
                if (k[0] < sm):
                    list1.append(k)
                else:
                    list2.append(k)
        if (len(list1) != 0):
            list.append(list1)
        if (len(list2) != 0):
            list.append(list2)
    cuttedArea.clear()
    for j in list:
        cuttedArea.append(j)
    list.clear()

a = 0

for i in cuttedArea:
    d = len(i)
    
    if a < d:
        a = d
print(a)