class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        ans = []
        
        smaller = collections.Counter()
        for x in changed:
            if x % 2 == 0 and x // 2 in smaller and smaller[x // 2] > 0:
                ans.append(x // 2)
                smaller[x // 2] -= 1
            else:
                smaller[x] += 1
        if len(ans) * 2 != len(changed):
            return []
        
        return ans
