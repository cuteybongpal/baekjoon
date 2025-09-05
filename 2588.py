a = input()
b = input()

res = []

for i in range(len(b)-1, -1, -1):
    res.append(int(b[i]) *int(a))

result = 0
idx = 0
for r in res:
    print(r)
    result += r * 10 ** idx
    idx += 1

print(result)
