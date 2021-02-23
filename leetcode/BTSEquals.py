# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_vals = []
        q_vals = []
        def getTreeVals(node,vals):
            if node:
                vals.append(node.val)  
                getTreeVals(node.left,vals)
                vals.append(None) if node.left == None else ""
                vals.append(None) if node.right == None else ""
                getTreeVals(node.right,vals)
        getTreeVals(p,p_vals)
        getTreeVals(q,q_vals)
        return p_vals == q_vals