# climbing stairs problem is the similar one to the fibonaci series 
def climstairs(n):
    prev = 0
    curr = 1
    for i in range(n):
        prev, curr = curr, prev + curr
    return curr