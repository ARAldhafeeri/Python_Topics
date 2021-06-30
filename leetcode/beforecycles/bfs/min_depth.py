from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([root])
        count = 0

        while queue:
            count += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    return count

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

    def maxDepth(self, root):
        level = 0
        queue = [root]
        if(root==None):
            return level
        else:
            while(queue != []):
                newQ = []
                for x in queue:
                    if x.children != []:
                        newQ = newQ + x.children
                level +=1
                queue = newQ
            return level

