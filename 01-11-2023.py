# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d={}
        def f(node):
            if not node:
                return
            d[node.val]=d.get(node.val,0)+1
            f(node.left)
            f(node.right)
        f(root)
        return [k for k,v in d.items() if max(d.values())==v]
        
