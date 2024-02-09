class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max_diff = 0

        nums = sorted(nums)
        max_diff = (nums[-1] * nums[-2]) - (nums[0] * nums[1])


        return max_diff

