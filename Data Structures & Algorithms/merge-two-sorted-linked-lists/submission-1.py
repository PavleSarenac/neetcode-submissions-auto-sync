# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        currentNode1, currentNode2 = list1, list2
        while currentNode1 and currentNode2:
            previousNode1 = None
            while currentNode1 and currentNode2 and currentNode1.val <= currentNode2.val:
                previousNode1 = currentNode1
                currentNode1 = currentNode1.next
            if previousNode1:
                previousNode1.next = currentNode2
            previousNode2 = None
            while currentNode1 and currentNode2 and currentNode2.val < currentNode1.val:
                previousNode2 = currentNode2
                currentNode2 = currentNode2.next
            if previousNode2:
                previousNode2.next = currentNode1
        return list1 if list1.val <= list2.val else list2

            