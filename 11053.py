a = int(input())
b = list(map(int, input().split()))

def binarySearch(t:list,c):
    l = 0
    h = len(t)
    while l < h:
        #중간
        mid = (l + h) //2
        #둘의 차이가 1이하일 경우 값 리턴 
        if (t[mid] < c):
            l = mid+1
        else:
            h = mid
    return l
t = []
for i in range(len(b)):
    
    idx = binarySearch(t, b[i])
    if idx == len(t):
        t.append(b[i])
    elif idx <= len(t) - 1:
        t[idx] = b[i]
    
print(len(t))