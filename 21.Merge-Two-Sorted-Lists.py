from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        new = another = ListNode()

        while list2 and list1:
            if list2.val > list1.val:
                new.next = list1
                list1 = list1.next
            else:
                new.next = list2
                list2 = list2.next
            new = new.next
        if list1:
            new.next = list1
        elif list2:
            new.next = list2

        return another.next
