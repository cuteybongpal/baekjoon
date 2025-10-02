from collections import deque
v, e = map(int, input().split())

path = {}
indegree = [0] * v
for i in range(e):
    origin, dest = map(int, input().split())
    if origin not in path:
        path[origin] = []
    path[origin].append(dest)
    indegree[dest-1] += 1
    
closed_list = []
q = deque()
for i in range(len(indegree)):
    if indegree[i] != 0:
        continue
    if (i+1) in closed_list:
        continue
    closed_list.append(i+1)
    q.append(i + 1)

while len(q) != 0:
    cur_node = q.popleft()
    print(cur_node, end=' ')
    if cur_node not in path:
        continue
    for i in path[cur_node]:
        if i in closed_list:
            continue
        indegree[i - 1] -= 1
        if indegree[i-1] > 0:
            continue
        q.append(i)
        closed_list.append(i)
        