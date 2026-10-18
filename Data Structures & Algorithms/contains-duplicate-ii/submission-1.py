class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k <= 0:
            return False
        leftWindowEdge = rightWindowEdge = 0
        slidingWindow = set()
        for number in nums:
            if number in slidingWindow:
                return True
            if rightWindowEdge - leftWindowEdge >= k:
                slidingWindow.remove(nums[leftWindowEdge])
                leftWindowEdge += 1
            slidingWindow.add(number)
            if rightWindowEdge < len(nums) - 1:
                rightWindowEdge += 1
        return False
