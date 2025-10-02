from collections import deque
y,x = map(int, input().split())
vertical_direction = [(1,0),(-1,0)]
horizontal_direction = [(0,1), (0, -1)]

floor = []
for i in range(y):
    fl = input()
    floor.append(fl)
closed = {}
q = deque()
def BFS(start):
    if start in closed:
        return False
    q.append(start)
    
    if floor[start[0]][start[1]] == '-':
        while len(q) != 0:
            cur_node = q.popleft()
            for i in horizontal_direction:
                next_x = i[1] + cur_node[1]
                if next_x < 0 or next_x >= x:
                    continue
                if (cur_node[0], next_x) in closed:
                    continue
                if floor[cur_node[0]][next_x] != '-':
                    continue
                q.append((cur_node[0], next_x))
                closed[(cur_node[0], next_x)] = 0
    else:
        while len(q) != 0:
            cur_node = q.popleft()
            for i in vertical_direction:
                next_y = i[0] + cur_node[0]
                if next_y < 0 or next_y >= y:
                    continue
                if (next_y, cur_node[1]) in closed:
                    continue
                if floor[next_y][cur_node[1]] != '|':
                    continue
                q.append((next_y, cur_node[1]))
                closed[(next_y, cur_node[1])] = 0
    return True
cnt = 0
for i in range(y):
    for j in range(x):
        if (i, j) in closed:
            continue
        BFS((i, j))
        cnt += 1
print(cnt)