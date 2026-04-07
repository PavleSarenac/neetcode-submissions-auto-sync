# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.mergeKListsHelper(lists, 0, len(lists) - 1)

    def mergeKListsHelper(self, originalList, startIndex, endIndex) -> Optional[ListNode]:
        if startIndex >= endIndex:
            return None
        
        middleIndex = (startIndex + endIndex) // 2

        self.mergeKListsHelper(originalList, startIndex, middleIndex)
        self.mergeKListsHelper(originalList, middleIndex + 1, endIndex)

        return self.mergeTwoLists(originalList, startIndex, middleIndex)

    def mergeTwoLists(self, originalList, startIndex, middleIndex) -> Optional[ListNode]:
        head1 = originalList[startIndex]
        head2 = originalList[middleIndex + 1]

        if head1.val <= head2.val:
            currentNode = head1
            head1 = head1.next
        else:
            originalList[startIndex], originalList[middleIndex + 1] = originalList[middleIndex + 1], originalList[startIndex]
            currentNode = head2
            head2 = head2.next

        finalHead = currentNode

        while head1 and head2:
            if head1.val <= head2.val:
                currentNode.next = head1
                head1 = head1.next
            else:
                currentNode.next = head2
                head2 = head2.next
            currentNode = currentNode.next

        while head1:
            currentNode.next = head1
            head1 = head1.next
            currentNode = currentNode.next

        while head2:
            currentNode.next = head2
            head2 = head2.next
            currentNode = currentNode.next

        return finalHead