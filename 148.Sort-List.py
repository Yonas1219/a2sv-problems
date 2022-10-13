# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result=[]
        current=head
        newhead=head
        while current:
            result.append(current.val)
            current=current.next
        result.sort()
        i=0
        while newhead:
            newhead.val=result[i]
            newhead=newhead.next
            i+=1
        return head
