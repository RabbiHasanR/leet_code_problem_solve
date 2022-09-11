def print_number(n):
    if n == 0:
        return
    
    print(n)
    print_number(n-1)
    print(n)

print_number(5)