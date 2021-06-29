"""
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Runtime: 160 ms, faster than 95.58% of Python3 online submissions for Sort List.
Memory Usage: 30.2 MB, less than 37.43% of Python3 online submissions for Sort List.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        nodes_vals = list()
        temp = head
        while temp:
            nodes_vals.append(temp.val)
            temp = temp.next
        temp = head
        nodes_vals = sorted(nodes_vals)
        i = 0
        while temp:
            temp.val = nodes_vals[i]
            i += 1
            temp = temp.next
        return head