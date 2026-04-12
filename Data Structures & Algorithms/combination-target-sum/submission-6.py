class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        allCombinations = []
        currentCombination = []

        def dfs(numIndex: int, target: int):
            if numIndex >= len(nums):
                return
            if target <= 0:
                if not target:
                    allCombinations.append(currentCombination.copy())
                return
            currentCombination.append(nums[numIndex])
            dfs(numIndex, target - nums[numIndex])
            currentCombination.pop()
            dfs(numIndex + 1, target)

        dfs(0, target)
        return allCombinations