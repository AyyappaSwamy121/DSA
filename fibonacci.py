 # 1. Brute Force / Iterative
def fibonacci_brute_force(n):
    if n <= 0:
        return []

    series = [0]

    if n == 1:
        return series

    series.append(1)

    for i in range(2, n):
        series.append(series[i - 1] + series[i - 2])

    return series


# 2. Recursion
def fibonacci_recursive(n):
    if n <= 0:
        return []

    def fib(k):
        if k <= 1:
            return k
        return fib(k - 1) + fib(k - 2)

    return [fib(i) for i in range(n)]


# 3. Dynamic Programming (Bottom-Up)
def fibonacci_dp(n):
    if n <= 0:
        return []

    if n == 1:
        return [0]

    dp = [0] * n
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp


# 4. Memoization (Top-Down)
def fibonacci_memoization(n):
    if n <= 0:
        return []

    memo = {}

    def fib(k):
        if k <= 1:
            return k

        if k in memo:
            return memo[k]

        memo[k] = fib(k - 1) + fib(k - 2)
        return memo[k]

    return [fib(i) for i in range(n)]


# Example
n = 10

print("Brute Force:   ", fibonacci_brute_force(n))
print("Recursion:      ", fibonacci_recursive(n))
print("Dynamic Prog.:  ", fibonacci_dp(n))
print("Memoization:    ", fibonacci_memoization(n))
