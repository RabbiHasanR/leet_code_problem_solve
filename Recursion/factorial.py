# factorial n! = n*(n-1)!

def factorial(n):
    if n < 0:
        return None
    if n in [0,1]:
        return 1
    return n * factorial(n-1)

print(factorial(7))