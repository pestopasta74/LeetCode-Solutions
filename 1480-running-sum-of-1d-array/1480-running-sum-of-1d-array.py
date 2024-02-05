class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_total = 0
        running_sum = []
        for num in nums:
            running_total += num
            running_sum.append(running_total)
        return running_sum
        