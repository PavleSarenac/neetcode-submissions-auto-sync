class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        final_x = init
        for i in range(iterations):
            final_x = final_x - learning_rate * 2 * final_x
        return round(final_x, 5)
