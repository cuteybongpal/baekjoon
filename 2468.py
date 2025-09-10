import sys
from collections import deque

n = int(sys.stdin.readline())
m = []

visited = [[-1]*n for _ in range(n)]

ma = 0
for i in range(n):
    mm = list(map(int, sys.stdin.readline().split()))
    m.append(mm)
    if ma < max(mm):
        ma = max(mm)

def bfs(maa:list, h:int, stamp:list, s):
    count = 0
    open_list = deque()
    b = []
    
    for i in range(len(maa)):
        for j in range(len(maa[i])):
            if maa[i][j] > h  and stamp[i][j] != s:
                b.append(0)
    while True:
        for i in range(n):
            isFind = False
            for j in range(n):
                if maa[i][j] > h and stamp[i][j] != s:
                    open_list.append((i, j))
                    stamp[i][j] = s
                    isFind = True
                    break
            if isFind:
                break
        
        while True:
            if len(open_list) == 0:
                break
            dd = open_list.popleft()
            b.pop()
            if dd[0]-1 >= 0 and stamp[dd[0]-1][dd[1]] != s:
                if maa[dd[0]-1][dd[1]] > h:
                    open_list.append((dd[0]-1, dd[1]))
                    stamp[dd[0]-1][dd[1]] = s
                    
            if dd[0]+1 < n and stamp[dd[0]+1][dd[1]] != s:
                if maa[dd[0]+1][dd[1]] > h:
                    open_list.append((dd[0]+1, dd[1])) 
                    stamp[dd[0]+1][dd[1]] = s
                    
            if dd[1]-1 >= 0 and stamp[dd[0]][dd[1]-1] != s:
                if maa[dd[0]][dd[1]-1] > h:
                    open_list.append((dd[0], dd[1]-1))
                    stamp[dd[0]][dd[1]-1] = s
                    
            if dd[1]+1 < n and stamp[dd[0]][dd[1]+1] !=s:
                if maa[dd[0]][dd[1]+1] > h:
                    open_list.append((dd[0], dd[1]+1))
                    stamp[dd[0]][dd[1]+1] = s
            
        count += 1
        if len(b) == 0:
            break
    
    return count

mmmax = 0
for i in range(ma):
    c = bfs(m, i, visited, i)
    if (c > mmmax):
        mmmax = c
    
    
print(mmmax)