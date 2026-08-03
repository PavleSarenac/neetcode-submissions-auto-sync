class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        f_n_minus_2 = 1
        f_n_minus_1 = 2
        for _ in range(3, n + 1):
            old_f_n_minus_1 = f_n_minus_1
            f_n_minus_1 = f_n_minus_1 + f_n_minus_2
            f_n_minus_2 = old_f_n_minus_1
        return f_n_minus_1