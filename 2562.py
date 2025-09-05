list = []
for i in range(9):
    list.append(int(input()))

idx = 0
max  = 0
for i in range(len(list)):
    if list[i] > max:
        max = list[i]
        idx = i+1

print(max)
print(idx)
