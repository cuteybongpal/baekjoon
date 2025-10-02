a = int(input())
b = list(map(int, input().split()))
b.sort()

def TwoPointerFind(start, end):
    s = start
    e = end
    min = 100000000000000000
    res = []
    while s < e:
        diff = b[s] + b[e]
        if diff == 0:
            return [b[s], b[e]]
        
        if min > abs(diff):
            min = abs(diff)
            res.clear()
            res.append(b[s])
            res.append(b[e])
        
        if diff < 0:
            s += 1
        else:
            e -= 1
    return res

result = TwoPointerFind(0, len(b)-1)  
print(result[0], result[1])