class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        allCombinations = []
        currentCombination = []

        def dfs(numIndex: int, target: int):
            if numIndex >= len(nums):
                return
            newTarget = target - nums[numIndex]
            if newTarget <= 0:
                if not newTarget:
                    allCombinations.append(currentCombination + [nums[numIndex]])
                return
            for i in range(numIndex, len(nums)):
                currentCombination.append(nums[numIndex])
                dfs(i, newTarget)
                currentCombination.pop()
                
        for numIndex in range(len(nums)):
            dfs(numIndex, target)

        return allCombinations