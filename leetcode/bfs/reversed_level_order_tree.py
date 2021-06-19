# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        hashtable = collections.defaultdict(list) # hashtable with lists and level keys
        deque = collections.deque([root]) # deque for performing bfs
        level = 0 # level key
        while deque:
            level_size = len(deque) # current level size
            for _ in range(level_size): #check all nodes in current level
                node = deque.popleft() # pop left from deque
                hashtable[level].append(node.val) # add  all nodes to current level in our hashtable
                # add child nodes to the queue
                if node.left: 
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            level += 1
        return list(reversed(hashtable.values())) # we got the level order in hashtable.values, now reverse it cuz that what the question is asking for