import heapq
f = []
for i in range(int(input())):
    s, e = map(int, input().split())
    f.append((s, e))
l = []
f.sort(key=lambda x: (x[1], x[0]))
late = f[0]
cnt = 1
for i in range(1, len(f)):
    if f[i][0] >= late[1]:
        late = f[i]
        cnt += 1
    
print(cnt)