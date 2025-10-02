a = int(input())
fibonacci_list = [0] * 100
fibonacci_list[1] = 1
def fibonacci(n:int):
    if n <= 1:
        return
    if fibonacci_list[n-1] == 0:
        fibonacci(n-1)
    fibonacci_list[n] = fibonacci_list[n-1] + fibonacci_list[n-2]
fibonacci(a)
print(fibonacci_list[a])