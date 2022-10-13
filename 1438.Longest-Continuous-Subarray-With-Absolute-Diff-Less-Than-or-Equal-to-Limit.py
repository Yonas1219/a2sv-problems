import collections
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQueue=collections.deque()
        maxQueue=collections.deque()
        answer=0
        i=0

        for j,ele in enumerate(nums):
            while minQueue and minQueue[-1]>ele:
                minQueue.pop()
            minQueue.append(ele)
            while maxQueue and maxQueue[-1]<ele:
                maxQueue.pop()
            maxQueue.append(ele)

            while maxQueue[0]-minQueue[0]>limit:
                if minQueue[0]==nums[i]:
                    minQueue.popleft()
                if maxQueue[0]==nums[i]:
                    maxQueue.popleft()
                i+=1
            answer=max(answer,j-i+1)

        return answer
