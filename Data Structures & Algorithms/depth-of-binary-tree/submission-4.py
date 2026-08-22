# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        height = 0
        max_d=0
        stack=[[root,height]]
        
        while stack:
            node, height = stack.pop()
            max_d = max(max_d,height)
            if node.left:
                stack.append([node.left, height+1])
            if node.right:
                stack.append([node.right,height+1])
            
        return max_d +1
        

