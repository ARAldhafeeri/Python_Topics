"""
Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

 

Example 1:



Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        vals=[]
        def inorder(node):
            if node:
                inorder(node.left)
                vals.append(node.val)
                inorder(node.right)
        def balance(l, r):
            if l<=r:
                mid = (l+r)//2
                cur = TreeNode(vals[mid])
                cur.left = balance(l, mid-1)
                cur.right = balance(mid+1, r)
                return cur
        inorder(root)
        n=len(vals)
        return balance(0, n-1)
        