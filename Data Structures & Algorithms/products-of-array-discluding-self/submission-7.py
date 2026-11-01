class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroElementIndex = -1
        
        prefixProducts = []
        prefixProduct = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroElementIndex = i
                prefixProduct = prefixProducts[i - 1] if i > 0 else 1
                break
            prefixProduct *= nums[i]
            prefixProducts.append(prefixProduct)

        suffixProducts = [0] * len(nums)
        suffixProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0 and i == zeroElementIndex:
                suffixProduct = suffixProducts[i + 1] if i < len(nums) - 1 else 1
                break
            if nums[i] == 0 and i != zeroElementIndex:
                suffixProduct = 0
                break
            suffixProduct *= nums[i]
            suffixProducts[i] = suffixProduct

        output = [0] * len(nums)
        if zeroElementIndex != -1:
            output[zeroElementIndex] = prefixProduct * suffixProduct
            return output

        for i in range(len(nums)):
            currentOutput = 1
            if i > 0:
                currentOutput *= prefixProducts[i - 1]
            if i < len(nums) - 1:
                currentOutput *= suffixProducts[i + 1]
            output[i] = currentOutput
        
        return output