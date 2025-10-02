# 0이 비워져있는 상태
# 1이 사과, 2는 뱀
from collections import deque

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N = int(input())
cur_dir = 1

mmap = []
for i in range(N):
    map_row = []
    for j in range(N):
        map_row.append(0)
    mmap.append(map_row)
K = int(input())

for i in range(K):
    x,y = map(int, input().split()) 
    mmap[x-1][y-1] = 1
L = int(input())
c = []
for i in range(L):
    inputs = input().split()
    X = int(inputs[0])
    C = inputs[1]
    c.append((X, C))

c.sort(key=lambda x: x[0])
moveQ = deque()
trail = deque()
trail.append((0, 0))
length = 1
for i in c:
    moveQ.append(i)
time = 0
while True:
    time += 1
    cur_pos = trail[-1]
    next_pos = (cur_pos[0] + direction[cur_dir][0], cur_pos[1] + direction[cur_dir][1])
    
    if next_pos[0] < 0 or next_pos[0] >= N or next_pos[1] < 0 or next_pos[1] >= N:
        break
    if mmap[next_pos[1]][next_pos[0]] == 1:
        length += 1
        
    cnt = 0
    trail.append(next_pos)
    for i in range(len(trail)):
        if trail[i] == next_pos:
            cnt += 1
            
    if cnt >= 2:
        break
    while len(trail) > length:
        p = trail.popleft()
        mmap[p[1]][p[0]] = 0
    
    
    mmap[next_pos[1]][next_pos[0]] = 2
    if len(moveQ) != 0 and moveQ[0][0] == time:
        ddd = moveQ.popleft()
        if ddd[1] == 'D':
            cur_dir = (cur_dir - 1) % len(direction)
        if ddd[1] == 'L':
            cur_dir = (cur_dir + 1) % len(direction)
print(time) 