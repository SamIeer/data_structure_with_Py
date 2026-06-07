# Fibonacci series fo the recursive way 
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib(n-1) + fib(n-2)


# Fibonacci series for the iterative eay DP
def fibi(n):
    prev = 0
    curr = 1
    for i in range(n):
        prev, curr = curr, prev + curr
    return prev 