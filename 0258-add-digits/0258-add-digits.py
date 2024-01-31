class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        while len(num) > 1:
            sum = 0  # Reset sum to 0 for each iteration
            for digit in num:
                sum += int(digit)
            num = str(sum)
        return int(num)
