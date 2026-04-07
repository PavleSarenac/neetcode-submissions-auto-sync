class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1Index = nums2Index = 0
        numsSorted = []
        while nums1Index < m and nums2Index < n:
            if nums1[nums1Index] <= nums2[nums2Index]:
                numsSorted.append(nums1[nums1Index])
                nums1Index += 1
            else:
                numsSorted.append(nums2[nums2Index])
                nums2Index += 1
        while nums1Index < m:
            numsSorted.append(nums1[nums1Index])
            nums1Index += 1
        while nums2Index < n:
            numsSorted.append(nums2[nums2Index])
            nums2Index += 1
        for i in range(m + n):
            nums1[i] = numsSorted[i]