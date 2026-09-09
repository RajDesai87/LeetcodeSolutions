# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        inc = 0
        dummyhead = ListNode(-1)
        pCurr = dummyhead
        while l1 is not None or l2 is not None:
            curr = inc
            if l1 is not None:
                curr += l1.val
                l1 = l1.next
            if l2 is not None:
                curr += l2.val
                l2 = l2.next
            inc = curr // 10
            curr = curr % 10
            pCurr.next = ListNode(curr,None)
            pCurr = pCurr.next
        if inc == 1:
            pCurr.next = ListNode(1, None)
        return dummyhead.next