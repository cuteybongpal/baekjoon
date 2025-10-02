import heapq

#힙큐 하나는 오름차순으로 다른 힙큐는 내림 차순으로 정렬했을 때 더 작은 게 중앙값임!
#힙큐 2개가 거의 같은 크기를 가질때만 그럼
hq1 = []
hq2 = []
#근데 어떻게 집어 넣을지 모르겠슴 ㅋㅋ
#중앙 값임이 성립하려면 둘의 크기 차이가 겨우 +- 1정도만 차이가 나야함
a = int(input())
result = []
for i in range(a):
    inp = int(input())
    if len(hq1) == 0:
        heapq.heappush(hq1, -inp)
        result.append(inp)
        continue
    
    if inp > -hq1[0]:
        heapq.heappush(hq2, inp)
    else:
        heapq.heappush(hq1, -inp)
    
    if len(hq2) - len(hq1) > 1:
        heapq.heappush(hq1, -heapq.heappop(hq2))
    elif len(hq1) - len(hq2) > 1:
        heapq.heappush(hq2, -heapq.heappop(hq1))
    
    if len(hq1) > len(hq2):
        result.append(-hq1[0])
    elif len(hq1) == len(hq2):
        result.append(-hq1[0])
    else:
        result.append(hq2[0])
for i in result:
    print(i)