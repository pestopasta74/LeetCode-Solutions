class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        new_nums = sorted(nums)
        highest_num = new_nums[-1]
        second_highest_num = new_nums[-2]

        if highest_num >= second_highest_num * 2:
            return nums.index(highest_num)
        
        return -1
        