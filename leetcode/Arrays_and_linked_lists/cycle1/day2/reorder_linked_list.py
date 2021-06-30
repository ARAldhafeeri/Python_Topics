"""

Runtime: 96 ms, faster than 51.89% of Python3 online submissions for Reorder List.
Memory Usage: 26.2 MB, less than 5.04% of Python3 online submissions for Reorder List.

Q:
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        hashtable = dict()
        n = 0
        curr = head
        while curr:
            hashtable[n] = curr
            n += 1
            curr = curr.next
            
        i = 0
        while(i < n//2 ):
            hashtable[i].next = hashtable[n - i - 1]
            hashtable[n - i - 1].next = hashtable[ i + 1]
            i += 1
        hashtable[i].next = None
            
        return hashtable.values()
            
            