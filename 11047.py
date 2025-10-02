c, k = map(int, input().split())

coins = []
for i in range(c):
    coins.append(int(input()))
    
def find(dest:int):
    l = 0
    h = len(coins) - 1
    while l < h:
        mid = (l + h) // 2
        if coins[mid] == dest:
            return coins[mid]
        if coins[mid] > dest:
            h = mid - 1
        else:
            l = mid + 1
    if coins[l] > dest:
        return coins[l-1]
    return coins[l]
cnt = 0
while k > 0:
    k -= find(k)
    cnt += 1
print(cnt)