import math
a = int(input())
al = list(map(int, input().split()))
b = int(input())
bl = map(int, input().split())

def find(ddd:list, dd:int):
    mid = len(ddd) // 2
    diff = len(ddd) - mid
    while True:
        if mid < 0 or mid >= len(ddd):
            return 0
        if ddd[mid] == dd:
            return 1
        if mid - 1 >= 0 and ddd[mid - 1] == dd:
            return 1
        if mid + 1 < len(ddd) and ddd[mid + 1] == dd:
            return 1
        if diff // 2 == 0:
            return 0
        if ddd[mid] > dd:
            mid = mid - math.ceil(diff / 2)
        else:
            mid = mid + math.ceil(diff / 2)
        diff = math.ceil(diff / 2)

al.sort()
for i in bl:
    print(find(al, i))