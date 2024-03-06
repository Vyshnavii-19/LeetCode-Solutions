# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        add=set()
        print(pos)
        if head==None or head.next == None:
            return False
        while head:
            if head in add:
                return True
            add.add(head)
            
            head=head.next
            
        return False
        