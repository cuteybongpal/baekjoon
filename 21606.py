import sys
sys.setrecursionlimit(1000)
n = int(input())

io = input()
nodes = []
for i in io:
    nodes.append(int(i))

path = {}
for i in range(n - 1):
    ori, dest = map(int, input().split())
    if ori not in path:
        path[ori] = []
    if dest not in path:
        path[dest] = []
    
    path[ori].append(dest)
    path[dest].append(ori)
cnt = 0
closed_list = {}
stack = []
def DFS():
    global cnt
    cur_node = stack.pop()
    for i in path[cur_node]:
        if i in closed_list:
            continue
        if nodes[i-1] == 1:
            cnt += 1
            continue
        stack.append(i)
        closed_list[i] = 0
        DFS()

for i in range(len(nodes)):
    if nodes[i] == 0:
        continue
    stack.append(i+1)
    closed_list[i+1] = 0
    DFS()
    stack.clear()
    closed_list.clear()
print(cnt)