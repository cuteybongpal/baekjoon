import math
n,c = map(int, input().split())

a = []

for i in range(n):
    a.append(int(input()))

a.sort()

def checkPlace(dist):
    global c
    curPos = a[0]
    count = 0
    for i in range(1, len(a)):
        # print(a[i] - curPos)
        if dist <= a[i] - curPos:
            curPos = a[i]
            count += 1
    # print(count)
    return count >= c-1
        
def check(low:int, high:int):
    d = 0
    if abs(high - low) <= 1:
        if c == 2:
            return low+1
        return low
    
    mid = (low + high) // 2
    # print(f"mid : {mid}")
    
    if checkPlace(mid):
        d = check(mid, high)
    else:
        d = check(low, mid)
    return d

print(check(0, a[-1] - a[0]))