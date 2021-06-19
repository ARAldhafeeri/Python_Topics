"""
Problem:
 You want to perform various calculations on dictionary ( min, max, sorting.. etc )
"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 73.20,
    'FB': 10.75,
}

min_price = min(zip(prices.values()))
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values()))
# max_price is (612.78, 'APPL')

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices) # {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 73.2, 'FB': 10.75}


def minDepth(self, root: TreeNode) -> int:
    # Solve with bfs
    if not root:
        return 0
    queue = [(root, 1)]
    while queue:
        node, depth = queue.pop(0)
        left = node.left
        right = node.right
        if not left and not right:
            return depth
        else:
            if left:
                queue.append((left, depth + 1))
            if right:
                queue.append((right, depth + 1))