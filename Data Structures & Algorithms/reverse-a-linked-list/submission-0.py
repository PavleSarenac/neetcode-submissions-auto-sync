# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentOldListNode = head
        currentNewListNode = previousNewListNode = None
        while currentOldListNode:
            currentNewListNode = ListNode(currentOldListNode.val, previousNewListNode)
            previousNewListNode = currentNewListNode
            currentOldListNode = currentOldListNode.next
        return currentNewListNode
