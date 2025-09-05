a = int(input())

count = 0
for i in range(1, a + 1):
    if i < 100:
        count += 1
        continue
    b = str(i)
    
    diff = int(b[0]) -int(b[1])
    if diff != int(b[1]) -int(b[2]):
        continue
    count += 1

print(count)