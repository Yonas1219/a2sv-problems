# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        current = head
        while current is not None:
            arr.append(current.val)
            current = current.next
            
        best = 0
        N = len(arr)
        for i in range(N):
            best = max(best, arr[i] + arr[N - i - 1])
        return best
