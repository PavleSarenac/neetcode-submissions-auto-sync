# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.diff = 0
        self.isBalanced = None
        self.postorderTraversal(root)
        if self.isBalanced == None:
            self.isBalanced = True
        return self.isBalanced

        
    def postorderTraversal(self, root: Optional[TreeNode]):
        if not root or self.isBalanced == False:
            return

        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)

        root.val = 0
        if root.left and not root.right:
            if root.left.val >= 1:
                self.isBalanced = False
            root.val += root.left.val + 1
        elif root.right and not root.left:
            if root.right.val >= 1:
                self.isBalanced = False
            root.val += root.right.val + 1
        elif root.left and root.right:
            if abs(root.left.val - root.right.val) > 1:
                self.isBalanced = False
            root.val += max(root.left.val, root.right.val) + 1
            