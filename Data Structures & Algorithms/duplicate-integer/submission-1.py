class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = dict()
        for num in nums:
            if hashMap.get(num):
                return True
            else:
                hashMap[num] = 1
        return False