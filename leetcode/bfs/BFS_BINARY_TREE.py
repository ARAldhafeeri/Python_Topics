# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return root==None or self.isSym(root.left,root.right)

    def isSym(self,left,right):
        if left==None and right==None:
            return True
        if left==None or right==None:
            return False
        return left.val==right.val and self.isSym(left.right,right.left) and self.isSym(right.right,left.left)
