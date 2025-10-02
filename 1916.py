import heapq
n = int(input())
e = int(input())

path = {}
for i in range(e):
    ori, dest, strength = map(int, input().split())
    if ori not in path:
        path[ori] = []
    path[ori].append((dest, strength))
start, end = map(int, input().split())
dist = [-1] * n

def BFS(start:int, end:int):
    q = []
    for i in path[start]:
        heapq.heappush(q, (i[1], start, i[0]))
    dist[start-1] = 0
    while len(q) != 0:
        cur_node = heapq.heappop(q)
        
        if dist[cur_node[2] - 1] <= cur_node[0] + dist[cur_node[1] - 1]  and dist[cur_node[2] - 1] != -1:
            continue
        if dist[end - 1] <= cur_node[0] + dist[cur_node[1] - 1] and dist[end - 1] != -1:
            continue
        dist[cur_node[2] - 1] = cur_node[0]
        if cur_node[2] == end:
            return 
        if cur_node[2] not in path:
            continue
        for i in path[cur_node[2]]:
            heapq.heappush(q, (i[1] + cur_node[0], cur_node[2], i[0]))
            
BFS(start, end)
print(dist[end-1])