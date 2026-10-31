class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSums = [nums[0]]
        for i in range(1, len(nums)):
            self.prefixSums.append(self.prefixSums[i - 1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSums[right]
        return self.prefixSums[right] - self.prefixSums[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)