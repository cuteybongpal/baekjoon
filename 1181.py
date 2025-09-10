a = int(input())
b = []

for i in range(a):
    b.append(input())
b.sort()
b.sort(key=len)

idx = 0
while idx < len(b) - 1:
    if b[idx] == b[idx + 1]:
        b.pop(idx)
        continue
    idx += 1


for i in b:
    print(i)