Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        hashtable = collections.defaultdict(collections.deque) # hashtable to store node vals for level we are working on
        dq = collections.deque([root]) # deque for preforming bfs
        level = 0 # keep track of levels as keys to our hashtable
        zigzag = False # to get zigzag level order traversal
        while dq:
            level_size = len(dq) # how many elements in the current level
            for _ in range(level_size): # check all nodes in the current level
                node = dq.popleft()
                if zigzag:
                    hashtable[level].append(node.val)
                else:
                    hashtable[level].appendleft(node.val)
                # put child nodes in the queue
                if node.right:
                    dq.append(node.right)
                if node.left:
                    dq.append(node.left)
            zigzag = not zigzag # toggle zigzag    
            level += 1 # next level
        return hashtable.values()