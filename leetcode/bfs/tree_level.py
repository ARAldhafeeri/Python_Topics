Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
          return []
        hashtable = collections.defaultdict(list) # hashtable to store node vals for level we are working on
        dq = collections.deque([root]) # deque for preforming bfs
        level = 0 # keep track of levels as keys to our hashtable
        while dq:
            level_size = len(dq) # how many elements in the current level
            for _ in range(level_size): # check all nodes in the current level
                node = dq.popleft()
                hashtable[level].append(node.val)
                # put child nodes in the queue
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            level += 1 # next level
        return hashtable.values()