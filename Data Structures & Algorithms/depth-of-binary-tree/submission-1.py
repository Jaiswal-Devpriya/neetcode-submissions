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
        '''height = 0
        stack=[root]
        seen=()
        while stack:
            curr= stack.pop()
            if curr not in seen:
                height+=1
                see.add(curr)
        
        max_h = max(h,max_h)'''
        return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))

