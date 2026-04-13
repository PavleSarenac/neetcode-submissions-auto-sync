class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        allCombinations = []
        currentCombination = []

        def dfs(numIndex: int, target: int):
            if numIndex >= len(nums):
                return
            if not target:
                allCombinations.append(currentCombination.copy())
                return
            newTarget = target - nums[numIndex]
            if newTarget < 0:
                return
            currentCombination.append(nums[numIndex])
            dfs(numIndex, newTarget)
            currentCombination.pop()
            dfs(numIndex + 1, target)

        nums.sort()
        dfs(0, target)
        return allCombinations