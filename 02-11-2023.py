#brute Force approch
Class Solution:
    def inorder(self,root,dictionary):
        if root is None:
            return
        dictionary[root]=0
        self.inorder(root.left,dictionary)
        self.inorder(root.right,dictionary)
    def order(self,root,arr):
        if root is None:
            return
        arr.append(root.val)
        self.order(root.left,arr)
        self.order(root.right,arr)
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        dictionary={}
        self.inorder(root,dictionary)
        # print(dictionary.values())
        count=0
        for i in dictionary:
            arr=[]
            self.order(i,arr)
            if i.val==sum(arr)//len(arr):
                count+=1
        return count


#Optiamal code
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def f(node):
            if not node:return 0,0
            ls,lc=f(node.left)
            rs,rc=f(node.right)
            s=ls+rs+node.val
            c=lc+rc+1
            if s//c==node.val:
                self.ans+=1
            return s,c
        f(root)
        return self.ans

            
