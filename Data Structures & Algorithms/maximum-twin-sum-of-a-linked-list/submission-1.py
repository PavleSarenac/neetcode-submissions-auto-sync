class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slowPointer = fastPointer = head
        previousNode = None
        while fastPointer and fastPointer.next:
            fastPointer = fastPointer.next.next
            nextNode = slowPointer.next
            slowPointer.next = previousNode
            previousNode = slowPointer
            slowPointer = nextNode

        firstHalfHead = previousNode
        secondHalfHead = slowPointer
        maxTwinSum = 0
        while firstHalfHead and secondHalfHead:
            twinSum = firstHalfHead.val + secondHalfHead.val
            maxTwinSum = max(maxTwinSum, twinSum)
            firstHalfHead = firstHalfHead.next
            secondHalfHead = secondHalfHead.next

        return maxTwinSum