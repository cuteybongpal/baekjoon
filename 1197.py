import heapq
node, edge = map(int, input().split())

path = {}
hq1 = []
for i in range(edge):
    origin, dest, strength = map(int, input().split())
    
    heapq.heappush(hq1, (strength, origin, dest))


def isCircling(element1, element2):
    print(element1, element2)
    print(parent)
    d1 = find(element1)
    d2 = find(element2)
    if d1 == d2:
        return False
    if size[d1] > size[d2]:
        
        parent[element2] = d1
        size[d2] -= 1
        size[d1] += 1
        for i in range(len(parent)):
            if parent[i] != d2:
                continue
            parent[i] = d1
            size[d2] -= 1
            size[d1] += 1
    else:
        parent[element1] = d2
        size[d2] += 1
        size[d1] -= 1
        for i in range(len(parent)):
            if parent[i] != d1:
                continue
            parent[i] = d2
            size[d1] -= 1
            size[d2] += 1
    return True
def find(x:int):
    if parent[x] == x:
        return x
    return find(parent[x])
parent = []
size = [1] * node
res = []
for i in range(node):
    parent.append(i)
print()
while len(hq1) != 0:
    item = heapq.heappop(hq1)
    isS = isCircling(item[1]-1, item[2]-1)
    if isS:
        res.append(item[0])
print(parent)
print(res)
print(sum(res))
