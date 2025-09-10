a = int(input())

b = list(map(int, input().split()))

list = []
def find(l1:list, l2:list, l3:list):
    if len(l2) != len(l1):
        for i in range(len(l1)):
            isDuplicate = False
            for j in l2:
                if j == i:
                    isDuplicate = True
                    break
            if not isDuplicate:
                l2.append(i)
                find(l1, l2, l3)
                l2.pop()
            
            
    else:
        sum = 0
        for i in range(len(l2) - 1):
            sum += abs(l1[l2[i]] - l1[l2[i+1]])
        l3.append(sum)

c = []
find(b, [], c)
print(max(c))