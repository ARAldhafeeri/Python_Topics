"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []

Runtime: 68 ms, faster than 73.18% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 17.2 MB, less than 23.40% of Python3 online submissions for Remove Linked List Elements.
"""

"""
sol: iterative.
The idea is to create dummy node one node before given head. Once we find the target
we create a temp node where we make prev node in head points to the next head
using the dummy linked list refrenced as (prev). then we delete the temp node
If the current node val is not target. Then previous become head,
head becomes curr.next
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        # create dummy linked list one node behind given head
        dummy = ListNode(-1)
        dummy.next = head
        prev, curr = dummy, head
        
        while curr:
            if curr.val == val:
                # Create temp Node;
                temp = curr
                prev.next = temp.next
                del temp
                curr = prev.next
            else:
                prev, curr = curr, curr.next
        return dummy.next
        