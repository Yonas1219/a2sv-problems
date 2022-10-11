class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s, res = 0, 0
        for i in range(0, k-1):
            s += arr[i]
            
        for i in range(k - 1, len(arr)):
            s += arr[i]
            if s / k >= threshold: res += 1
            s -= arr[i - k + 1]
                
        return res
