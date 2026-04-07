# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        preorderRoot = TreeNode(preorder[0])
        inorderRootIndex = inorder.index(preorderRoot.val)
        preorderRoot.left = self.buildTree(preorder[1: inorderRootIndex + 1], inorder[: inorderRootIndex])
        preorderRoot.right = self.buildTree(preorder[inorderRootIndex + 1: ], inorder[inorderRootIndex + 1: ])
        return preorderRoot