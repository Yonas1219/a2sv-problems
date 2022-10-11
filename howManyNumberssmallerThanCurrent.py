class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        buckets = [0] * 101
        for num in nums:
            buckets[num] += 1
        acc = 0
        for i in range(len(buckets)):
            prev = buckets[i]
            buckets[i] = acc
            acc += prev
        return [buckets[num] for num in nums]
