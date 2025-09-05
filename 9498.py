a = int(input())

grade = ''
if a >= 90 and a <= 100:
    grade = 'A'
elif a >=  80:
    grade = 'B'
elif a >= 70:
    grade = 'C'
elif a >= 60:
    grade = 'D'
else:
    grade = 'F'

print(grade)