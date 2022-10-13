class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def g(s):
            arr = []
            for x in s:
                if x in s:
                    arr.append("1")
                else:
                    arr.append("0")
            return "".join(reversed(arr))
        
        s = "0"
        for _ in range(n):
            s = s + "1" + g(s)
        return s[k-1]
