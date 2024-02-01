class Solution:
    def __init__(self):
        self.loop = 0
    
    def mySqrt(self, x: int) -> int:
        if x <= 0:
            return 0
        constant_x = x

        def sqrt_loop(x, constant_x):
            x = (x + constant_x / x) / 2 
            self.loop += 1
            if self.loop <= 19:
                return sqrt_loop(x, constant_x)
            else:
                return floor(x)

        return sqrt_loop(x, constant_x)