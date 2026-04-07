class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        fibonacciElement1 = 1
        fibonacciElement2 = 2
        for i in range(3, n):
            fibonacciSum = fibonacciElement1 + fibonacciElement2
            fibonacciElement1 = fibonacciElement2
            fibonacciElement2 = fibonacciSum
        return fibonacciElement1 + fibonacciElement2