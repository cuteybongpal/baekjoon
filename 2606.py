v = int(input())
e = int(input())

rank = [1] * v
parent = []
connection = []

for i in range(v):
    parent.append(i)
for i in range(e):
    ori, dest = map(int, input().split())
    connection.append((ori-1, dest-1))


def find(element:int):
    if element == parent[element]:
        return element
    return find(parent[element])
def add(element1:int, element2:int):
    d1 = find(element1)
    d2 = find(element2)
    if d1 == d2:
        return
    
    if rank[d1] > rank[d2]:
        for i in range(len(parent)):
            if parent[i] != d2:
                continue
            parent[i] = d1
            rank[d2] -= 1
            rank[d1] += 1
    else:
        for i in range(len(parent)):
            if parent[i] != d1:
                continue
            parent[i] = d2
            rank[d2] += 1
            rank[d1] -= 1
for i in connection:
    add(i[0], i[1])
print(rank[parent[0]]-1)