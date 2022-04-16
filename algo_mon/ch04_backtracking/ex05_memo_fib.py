def fib(n):
    if n == 0 or n == 1:
        return n

    return fib(n - 1) + fib(n - 2)

def fib(n, memo):
    if n in memo:
        return memo[n]

    if n == 0 or n == 1:
        return n

    res = fib(n - 1, memo) + fib(n - 2, memo)

    memo[n] = res
    return res

memo = {}
fib(70, memo)

print(memo)