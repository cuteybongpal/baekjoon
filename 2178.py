from collections import deque
dirs = [(1,0), (0,1), (-1,0), (0,-1)]

destY, destX = map(int, input().split())
mm = []
for i in range(destY):
    mm.append(input())
    
q = deque()
q.append((0, 0))
closed_list = [(0,0)]
dist = {(0,0) : 0}
while len(q) != 0:
    cur_pos = q.popleft()
    closed_list.append(cur_pos)
    isArrived = False
    for i in dirs:
        next_pos_x = i[1] + cur_pos[1]
        next_pos_y = i[0] + cur_pos[0]
        
        if (next_pos_y, next_pos_x) in closed_list:
            continue
        if next_pos_x < 0 or next_pos_y < 0:
            continue
        if next_pos_x >= destX or next_pos_y >= destY:
            continue
        if mm[next_pos_y][next_pos_x] == '0':
            continue
        q.append((next_pos_y, next_pos_x))
        dist[(next_pos_y, next_pos_x)] = dist[cur_pos] + 1
        closed_list.append((next_pos_y, next_pos_x))
        if (next_pos_y, next_pos_x) == (destY-1, destX-1):
            isArrived = True
            break
    if isArrived:
        break
print(dist[(destY - 1, destX - 1)]+1)