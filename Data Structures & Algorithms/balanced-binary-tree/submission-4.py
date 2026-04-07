class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0

            left = height(node.left)
            if left == -1:
                return -1  # early exit

            right = height(node.right)
            if right == -1 or abs(left - right) > 1:
                return -1  # early exit

            return 1 + max(left, right)

        return height(root) != -1