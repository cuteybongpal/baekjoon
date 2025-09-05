year = int(input())

isyoon = 0

if year % 4 == 0 and year % 100 != 0:
    isyoon = 1
elif year % 400 == 0:
    isyoon = 1

print(isyoon)