class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        idx=0
        res=ListNode()
        res.next=list1
        node=res
        while node:
            if idx==a:
                tmp=node.next
                node.next=list2
                node=tmp
            elif idx==b+1:
                while list2.next:
                    list2=list2.next
                list2.next=node.next
                break
            else:
                node=node.next
            idx+=1
        return res.next