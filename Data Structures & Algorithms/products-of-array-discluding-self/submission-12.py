class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProducts = [0] * len(nums)
        prefixProduct = 1
        for i in range(len(nums)):
            prefixProducts[i] = prefixProduct
            prefixProduct *= nums[i]

        suffixProducts = [0] * len(nums)
        suffixProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            suffixProducts[i] = suffixProduct
            suffixProduct *= nums[i]

        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = prefixProducts[i] * suffixProducts[i]
        
        return output