class Solution:
    def kthLargestNumber(self, arr: List[str], k: int) -> str:
        arr = [int(arr[i]) for i in range(len(arr))]
        arr.sort(reverse=True)
        return str(arr[k - 1])
