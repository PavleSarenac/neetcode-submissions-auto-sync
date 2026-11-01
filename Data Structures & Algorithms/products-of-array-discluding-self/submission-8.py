class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroElementIndex = -1
        
        prefixProducts = []
        prefixProduct = 1
        for i in range(len(nums)):
            prefixProduct *= nums[i]
            prefixProducts.append(prefixProduct)

        suffixProducts = [0] * len(nums)
        suffixProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            suffixProduct *= nums[i]
            suffixProducts[i] = suffixProduct

        output = [0] * len(nums)
        for i in range(len(nums)):
            currentOutput = 1
            if i > 0:
                currentOutput *= prefixProducts[i - 1]
            if i < len(nums) - 1:
                currentOutput *= suffixProducts[i + 1]
            output[i] = currentOutput
        
        return output