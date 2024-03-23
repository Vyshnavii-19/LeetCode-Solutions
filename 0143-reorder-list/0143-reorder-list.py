class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        # find the middle node `prev`
        # for [1,2,3,4,5] prev will be pointing at 3
        # for [1,2,3,4] prev will be pointing at 2
        # first half is equal or one longer than 2nd half
        mid = head
        tail = head
        prev = None
        while tail:
            prev = mid
            mid = mid.next            
            tail = tail.next
            if tail:
                tail = tail.next
        
        # cut off the first haf
        prev.next = None
        
        # reverse the 2nd half
        prev = None
        curr = mid
        while curr:
            n = curr.next
            curr.next = prev            
            prev = curr
            curr = n        
        tail = prev
        
        #print(tail)
        #print(head)
        # merge the two
        begin = head
        while begin and tail:
            n = begin.next
            tn = tail.next
            
            begin.next = tail
            tail.next = n
                        
            begin = n
            tail = tn