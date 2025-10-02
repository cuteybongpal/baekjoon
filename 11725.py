from collections import deque
a = int(input())
parent = []

path = {}
for i in range(a-1):
    ori, dest = map(int, input().split())
    if ori not in path:
        path[ori] = []
    if dest not in path:
        path[dest] = []
    path[ori].append(dest)
    path[dest].append(ori)

q = deque()
q.append(1)
visited = [False] * a
visited[0] = True
parent = [0] * a

while len(q) != 0:
    cur_node = q.popleft()
    if cur_node not in path:
        continue
    for i in path[cur_node]:
        if visited[i-1]:
            continue
        visited[i-1] = True
        parent[i-1] = cur_node
        q.append(i)

for i in range(1, len(parent)):
    print(parent[i])