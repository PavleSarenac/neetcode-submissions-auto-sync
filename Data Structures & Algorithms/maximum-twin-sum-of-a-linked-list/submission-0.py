# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        listSize = 0
        currentNode = head
        while currentNode:
            listSize += 1
            currentNode = currentNode.next
        leftHalfEndIndex = listSize // 2 - 1

        firstListHalfValues = dict()
        currentNode = head
        for nodeIndex in range(leftHalfEndIndex + 1):
            firstListHalfValues[nodeIndex] = currentNode.val
            currentNode = currentNode.next

        maxTwinSum = 0
        for nodeIndex in range(leftHalfEndIndex + 1, listSize):
            twinIndex = listSize - 1 - nodeIndex
            twinSum = firstListHalfValues[twinIndex] + currentNode.val
            maxTwinSum = max(maxTwinSum, twinSum)
            currentNode = currentNode.next

        return maxTwinSum
