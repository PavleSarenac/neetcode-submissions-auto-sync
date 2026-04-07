class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        scannedNumbers = set()
        for num in nums:
            if num in scannedNumbers:
                return True
            scannedNumbers.add(num)
        return False