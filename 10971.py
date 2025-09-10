a = int(input())
d = []
for i in range(a): 
    b = list(map(int, input().split()))
    d.append(b)

def tour(l1:list,l2:list,l3:list , idx:int):
    if len(l1) > len(l2) - 1:
        for i in range(len(l1[idx])):
            if i in l2:
                continue
            if l1[idx][i] == 0:
                continue
            l2.insert(-1, i)
            tour(l1, l2, l3, i)
            l2.pop(-2)
    else:
        if (l1[idx][l2[0]] != 0):
            s = 0
            #print(l2)
            for i in range(len(l2) - 1):
                s += l1[l2[i]][l2[i+1]]
            l3.append(s)
            return
        for i in range(len(l1[idx])):
            if l1[idx][i] == 0:
                continue
            if i in l2:
                continue
            l2.insert(-1, i)
            tour(l1, l2, l3, idx)
            l2.pop(-1)

c = []
for i in range(a):
    tour(d, [i, i], c, i)
    
print(min(c))