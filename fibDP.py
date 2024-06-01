def fibDP_1(n):
    l, r = 0, 1
    for i in range(n):
        l, r = r, l + r
    return l

def fibDP_2(n):
    if n <= 0:
        return 0
    
    fib = [0] * (n+1)
    fib[1] = 1

    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]

    return fib[n]

print(fibDP_1(5))
print(fibDP_2(5))