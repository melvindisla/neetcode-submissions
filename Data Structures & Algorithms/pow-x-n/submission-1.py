class Solution:
    def myPow(self, x: float, n: int) -> float:
        # in useing recursion we would need some base cases

        #1. if x == 1 or x == 0, return 0
        #2. if n == 0, return 1
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        res = 1
        power = abs(n)
        
        while power:
            if power & 1:
                res *= x
            x *= x
            power >>= 1
        
        return res if n >= 0 else 1 / res