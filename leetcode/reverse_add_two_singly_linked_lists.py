# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stringL1 = ''
        stringL2 = ''
        while (l1 != None) | (l2 != None):
            if(l1 != None):
                stringL1 += str(l1.val)
                l1 = l1.next
            if(l2 !=None):
                stringL2 += str(l2.val)
                l2= l2.next
        stringL1 = ''.join(list(reversed(stringL1)))
        stringL2 = ''.join(list(reversed(stringL2)))
        magicNumber = int(stringL1) + int(stringL2)
        magicNumber = list(str(magicNumber))

        cur = dummy = ListNode(0)
        for i in list(reversed(magicNumber)):
            cur.next = ListNode(int(i))
            cur = cur.next
        return dummy.next
