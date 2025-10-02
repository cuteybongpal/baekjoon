import math
import sys
N, M = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))

ssum = 0
low = 0
high = max(trees)
while abs(low - high) > 1:
    mid = (high + low) //2
    ssum = 0
    for i in trees:
        if i < mid:
            continue
        s = i - mid
        ssum += s
    if (ssum < M):
        high = mid
    else:
        low = mid
print(low)