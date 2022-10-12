class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        N = len(arr)
        
        counts = collections.Counter(arr)
        vs = sorted(counts.values(), key=lambda x: -x)
        
        total = N
        for i, x in enumerate(vs):
            total -= x
            
            if total * 2 <= N:
                return i + 1
