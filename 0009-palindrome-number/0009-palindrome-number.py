class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        forwards = x
        backwards = x[::-1]
        if forwards == backwards:
            return True
        return False

        