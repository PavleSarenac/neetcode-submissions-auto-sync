class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubsets = []
        currentSubset = []

        def dfs(numIndex: int):
            if numIndex >= len(nums):
                allSubsets.append(currentSubset.copy())
                return
            currentSubset.append(nums[numIndex])
            dfs(numIndex + 1)
            currentSubset.pop()
            dfs(numIndex + 1)
        
        dfs(0)
        return allSubsets