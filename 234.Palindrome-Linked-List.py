# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        array = []
        while head:
            array.append(head.val)
            head = head.next
        first = 0
        last = len(array) - 1
        while first < last:
            if array[first] != array[last]:
                return False
            first += 1
            last -= 1
        return True
