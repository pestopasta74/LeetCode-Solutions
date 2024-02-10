import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Check if n is a positive integer
        if n <= 0:
            return False
        
        # Compute the logarithm base 2
        log_n = math.log2(n)
        
        # Check if the logarithm is an integer
        if log_n.is_integer():
            return True
        else:
            return False
