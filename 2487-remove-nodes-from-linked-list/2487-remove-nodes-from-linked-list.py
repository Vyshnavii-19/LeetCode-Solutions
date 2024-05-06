# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        head = self._reverse(head)
        prev, current = head, head.next
        while current:
            if prev.val > current.val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        
        return self._reverse(head)


    def _reverse(self, head: ListNode) -> ListNode:
        prev, current = None, head
        while current:
            _next = current.next
            current.next = prev
            prev = current
            current = _next
        return prev
        