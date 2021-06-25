"""

Q:  Given a linked list, return the node where the cycle begins. If there is no cycle, return null.


Runtime: 52 ms, faster than 60.68% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 17.7 MB, less than 8.92% of Python3 online submissions for Linked List Cycle II.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visted = set()
        curr = head
        while curr:
            if curr in visted:
                return curr
            else:
                visted.add(curr)
            curr = curr.next
        return None
        
        