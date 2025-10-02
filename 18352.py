from collections import deque

n, e, k, s = map(int, input().split())

edges = {}

for i in range(e):
    origin, dest = map(int, input().split())
    if origin not in edges:
        edges[origin] = []
    edges[origin].append(dest)
res = []
dist = [0] * n
def BFS(start:int) -> int:
    q = deque()
    closed_list = [start]
    q.append(start)
    while len(q) != 0:
        cur_node = q.popleft()
        if dist[cur_node-1] > k:
            return
        if cur_node in edges:
            for i in edges[cur_node]:
                if i in closed_list:
                    continue
                if i in q:
                    continue
                dist[i-1] = dist[cur_node-1]+1
                if dist[i-1] == k:
                    res.append(i)
                closed_list.append(i)
                q.append(i)
BFS(s)
res.sort()
if len(res) != 0:
    for i in res:
        print(i)
else:
    print(-1)