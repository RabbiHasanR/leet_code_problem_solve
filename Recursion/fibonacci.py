# fibonacci = (n-2) + (n-1)

def fibonacci(n):
    if n in [1,2]:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(9))