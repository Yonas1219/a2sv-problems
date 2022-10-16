# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res = []
        stack = []
        i = 0
        ptr = head
        while ptr is not None:
            res.append(0)
            if len(stack) == 0 or ptr.val < stack[-1][0]:
                stack.append((ptr.val, i))
            else:
                while len(stack) > 0 and ptr.val > stack[-1][0]:
                    res[stack[-1][1]] = ptr.val
                    stack.pop()
                stack.append((ptr.val, i))
            ptr = ptr.next
            i += 1
        return res
            
