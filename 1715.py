import heapq

hq = []
a = int(input())

for i in range(a):
    heapq.heappush(hq, int(input()))

result = 0

while len(hq) != 1:
    res = 0
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    result += (a + b)
    res = a + b
    heapq.heappush(hq, res)

print(result)