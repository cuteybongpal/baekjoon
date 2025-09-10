a = int(input())
list = []

for i in range(a):
    list.append(int(input()))
    
for i in range(len(list)):
    for j in range(len(list) - i-1):
        if list[j+1] < list[j]:
            list[j+1], list[j] = list[j], list[j+1]
            
for i in list:
    print(i)