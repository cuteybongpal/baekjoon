n  = int(input())
numbers = list(map(int, input().split()))
ops = list(map(int, input().split()))
res = []

def DFS(number:int, idx:int):
    for i in range(len(ops)):
            if ops[i] == 0:
               continue
            num = 0
            if i == 0:
                num = number + numbers[idx]
            elif i == 1:
                num = number - numbers[idx]
            elif i == 2:
                num = number * numbers[idx]
            elif i == 3:
                num = int(number / numbers[idx])
            ops[i] -= 1
            print(f"deps : {idx}, {ops}")
            if idx < len(numbers)-1:
                DFS(num, idx+1)
            else:
                print(num)
                res.append(num)
            ops[i] += 1
DFS(numbers[0], 1)
print(max(res))
print(min(res))
