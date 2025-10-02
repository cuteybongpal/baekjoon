import sys
a = int(sys.stdin.readline())

b = []

for i in range(a):
    pos, radius = map(int, sys.stdin.readline().split())
    b.append((pos - radius, pos + radius))

b = sorted(b, key=lambda t: (t[0], -t[1]))
count = 0
stack1 = []
stack2 = []
for i in range(len(b)):
    if len(stack2) == 0:
        stack1.append(1)
        stack2.append(b[i])
        continue
    lastR = None
    curL = b[i][0]
    while len(stack2) != 0 and stack2[-1][1] <= curL:
        if lastR is not None and lastR < stack2[-1][1]:
            stack1.append(0)
        stack1.append(-1)
        lastR = stack2.pop()[1]
    
    if stack1[-1] == 1 and stack2[-1][0] < curL:
        stack1.append(0)
    elif stack1[-1] == -1 and lastR is not None and lastR < curL:
        stack1.append(0)
    stack1.append(1)
    stack2.append(b[i])
    
    if i == len(b) - 1:
        h = None
        while len(stack2) != 0:
            if h is not None and stack2[-1][1] > h[1]:
                stack1.append(0)
            stack1.append(-1)
            h = stack2.pop()
isDevided = []
length = []
cnt = 1
for i in stack1:
    if i == 1:
        stack2.append(0)
        isDevided.append(False)
        if len(length) != 0:
            length[-1] = length[-1] + 1
        length.append(0)
        cnt += 1
    elif i == -1:
        if not isDevided[-1] and length[-1] != 0:
            cnt += 1
        stack2.pop()
        isDevided.pop()
        
        length.pop()
    elif i == 0:
        if len(stack2) == 0:
            continue
        isDevided[-1] = True
        length[-1] = length[-1] + 1

sys.stdout.write(str(cnt))