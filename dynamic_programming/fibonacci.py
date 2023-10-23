from utils.utils import measure_execution_time


# pros: Faster run time
# cons: Ordering of subproblems matter
@measure_execution_time
def bottom_up_fibonacci(n: int) -> int:
    if n <= 1:
        return n

    # list of size n+1
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


# pros: Easier to read
# cons: RecursionError at large n even with memoization
memo = {}
@measure_execution_time
def top_down_fibonacci(i: int) -> int:
    if i <= 1:
        return i
    if i not in memo.keys():
        memo[i] = top_down_fibonacci(i-1) + top_down_fibonacci(i-2)
    return memo[i]

n = 50000
print(bottom_up_fibonacci(n))
print(top_down_fibonacci(n))