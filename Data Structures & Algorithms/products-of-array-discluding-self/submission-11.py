class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        
        prefixProduct = 1
        for i in range(len(nums)):
            output[i] = prefixProduct
            prefixProduct *= nums[i]

        suffixProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suffixProduct
            suffixProduct *= nums[i]

        return output