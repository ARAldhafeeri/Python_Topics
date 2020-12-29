# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        ans = []
        for node in lists:
            curr = node
            while curr:
                ans.append(curr.val)
                curr = curr.next
        ans = sorted(ans)

        current = dummy = ListNode(0)
        for value in ans:
            current.next = ListNode(value)
            current = current.next
        return dummy.next
