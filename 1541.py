ops = input()
d = ops.split('-')
res = 0
for i in range(len(d)):
    s = 0
    for j in d[i].split('+'):
        s += int(j)
    if i == 0:
        res += s
    else:
        res -= s
print(res)