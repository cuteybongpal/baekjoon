from collections import deque

N, K = map(int, input().split())
Q = deque()
cnt = 0
list = []
 
for i in range(N):
    Q.append(i+1)


while len(Q) != 0:
    tmp = Q.popleft()
    cnt += 1
    
    if cnt == K:
        cnt = 0
        list.append(tmp)
    else:
        Q.append(tmp)
s = ", ".join(map(str, list))
print(f"<{s}>")