from collections import deque


a = int(input())
Q = deque()
for i in range(a):
    Q.append(i+1)
    
idx = 0
while len(Q) >= 2:
    tm= Q.popleft()
    if idx % 2 != 0:
        Q.append(tm)
    idx += 1
        
print(Q.popleft())