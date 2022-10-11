class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        
        left = 0
        ans = 0
        
        while left < n:
            #find the string point of increasing sequence
            while left < n - 1 and arr[left] >= arr[left + 1]:
                left += 1
            # now move the right pointer
            right = left + 1
            # find the end of increasing sequence
            while right < n - 1 and arr[right] < arr[right + 1]:
                right += 1
            # try to find the deceasing sequence
            while right < n - 1 and arr[right] > arr[right + 1]:
                right += 1
                ans = max(ans, right-left + 1)
            left = right
        return ans
