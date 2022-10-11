# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        
        while cur:
            #if next two nodes are duplicates move the cur.next forward
            if cur.next and cur.next.next and cur.next.val == cur.next.next.val:
                temp = cur.next.next
                while temp and temp.next and temp.val == temp.next.val:
                    temp = temp.next
                cur.next = temp.next
            else:
            #if next two nodes are not duplicates move the cur to cur.next forward
                cur = cur.next
        return dummy.next
