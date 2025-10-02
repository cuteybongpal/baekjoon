from collections import deque
import sys
a = int(sys.stdin.readline())

res = []
def BFS(cnt:int):
    while len(q) != 0:
        cur_node = q.popleft()
        if cur_node not in path:
            continue
        for j in path[cur_node]:
            if visited[j-1] == visited[cur_node-1]:
                if len(res) <= cnt:
                    res.append('NO')
                return
            if visited[j-1] != -1:
                continue
            q.append(j)
            visited[j-1] = (visited[cur_node-1] + 1) % 2

for i in range(a):
    n, e = map(int, sys.stdin.readline().split())
    path = {}
    for j in range(e):
        ori, dest = map(int, sys.stdin.readline().split())
        if ori not in path:
            path[ori] = []
        if dest not in path:
            path[dest] = []
        path[ori].append(dest)
        path[dest].append(ori)
    q = deque()
    visited = [-1] * n
    for ii in range(len(visited)):
        if visited[ii] != -1:
            continue
        q.append(ii+1)
        visited[ii] = 0
        BFS(i)
    if i == len(res):
        res.append('YES')
sys.stdout.write("\n".join(res))