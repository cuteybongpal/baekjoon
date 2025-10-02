from collections import deque
import sys
sys.setrecursionlimit(10000)

v, e, r = map(int, input().split())
m = []

for i in range(v):
    dest = []
    for j in range(v):
        dest.append(0)
    m.append(dest)

for i in range(e):
    ori, dest = map(int, input().split())
    m[ori-1][dest-1] = 1
    m[dest-1][ori-1] = 1
print(m)

def BFS(mmap:list, start:int):
    q = deque()
    isSearched = [False] * v
    isSearched[start] = True
    q.append(start)
    while len(q) != 0:
        cur_node = q.popleft()
        isSearched[cur_node] = True
        for i in range(len(mmap[cur_node])):
            if isSearched[i] or i in q or mmap[cur_node][i] == 0:
                continue
            q.append(i)
        print(f"{cur_node+1}", end=' ')


def DFS(mmap:list, node:int, isSearched:list):
    print(node+1, end=' ')
    isSearched[node] = True
    for i in range(len(mmap[node])):
        if isSearched[i] or mmap[node][i] == 0:
            continue
        DFS(mmap, i, isSearched)
DFS(m, r-1, [False]*v)   
print()
BFS(m, r-1)