a = int(input())
fibonacci_list = [0, 1]

for i in range(a):
    fibonacci_list.append((fibonacci_list[-1] + fibonacci_list[-2]) % 15746)
print(fibonacci_list[-1])