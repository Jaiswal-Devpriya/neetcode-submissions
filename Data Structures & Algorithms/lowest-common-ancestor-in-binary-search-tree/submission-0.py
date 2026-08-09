# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
        if root is p or root is q:
            return root
        left_result = self.lowestCommonAncestor(root.left,p,q)
        right_result = self.lowestCommonAncestor(root.right,p,q)
        if left_result is not None and right_result is not None:
            return root
        if left_result is not None:
            return left_result
        else:
            return right_result

        