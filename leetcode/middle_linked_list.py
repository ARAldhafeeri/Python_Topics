# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        ans = []
        while head:
            ans.append(head)
            head = head.next
        target = len(ans) // 2
        return ans[target]
