from collections import deque
import sys
input = sys.stdin.readline

directions = [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1, 0, 0)]
m, n, h = map(int, input().split())
mm = []
q = deque()
closed_list = {}
max_cnt = n * m * h
cnt = 0
days = {}

for i in range(h):
    z = []
    for j in range(n):
        x = list(map(int, input().split()))
        for k in range(len(x)):
            if x[k] != 1:
                if x[k] == -1:
                    max_cnt -= 1
                continue
            q.append((i, j, k))
            closed_list[(i, j, k)] = 0 
            days[(i,j,k)] = 0
            cnt += 1
        z.append(x)
    mm.append(z)

cur_node = 0
while len(q) != 0:
    cur_node = q.popleft()
    for i in directions:
        next_h = i[2] + cur_node[0]
        next_n = i[1] + cur_node[1]
        next_m = i[0] + cur_node[2]
        g = (next_h, next_n, next_m)
        if next_h < 0 or next_n < 0 or next_m < 0:
            continue
        if next_h >= h or next_n >= n or next_m >= m:
            continue
        if mm[next_h][next_n][next_m] != 0:
            continue
        if g in closed_list:
            continue
        q.append(g)
        closed_list[g] = 0
        cnt += 1
        days[g] = days[cur_node] + 1
        
if cnt != max_cnt:
    print(-1)
else:
    print(days[cur_node])