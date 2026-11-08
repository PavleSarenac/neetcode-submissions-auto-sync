class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slowPointer = fastPointer = 0
        while slowPointer != fastPointer or slowPointer == 0:
            slowPointer = nums[slowPointer]
            fastPointer = nums[nums[fastPointer]]

        slowPointer2 = 0
        while slowPointer2 != slowPointer:
            slowPointer2 = nums[slowPointer2]
            slowPointer = nums[slowPointer]

        return slowPointer2