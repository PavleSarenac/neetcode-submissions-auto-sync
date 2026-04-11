# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.currentSum = 0
        def backtrack(root: Optional[TreeNode]) -> bool:
            if not root:
                return False
            
            self.currentSum += root.val

            if not root.left and not root.right and self.currentSum == targetSum:
                return True

            if backtrack(root.left):
                return True
            if backtrack(root.right):
                return True

            self.currentSum -= root.val
            return False
        return backtrack(root)