class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        my_dict = {}
        # my_dict = {1:2,2:1,3:1}
        n_good_pairs = 0
        for num in nums:
            if num in my_dict:
                n_good_pairs = n_good_pairs + my_dict[num]
                my_dict[num] = my_dict[num] + 1
            else:
                my_dict[num] = 1
        return n_good_pairs
