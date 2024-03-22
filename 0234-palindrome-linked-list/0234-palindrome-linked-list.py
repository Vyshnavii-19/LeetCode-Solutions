# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        pre = None
        while fast and fast.next:
            fast = fast.next.next
            next = slow.next
            slow.next = pre
            pre = slow
            slow = next
        if fast: slow = slow.next
        while pre and slow:
            if pre.val != slow.val: return False
            pre, slow = pre.next, slow.next
        return True