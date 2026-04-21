class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        if x<4:
            return 1
        r=2
        while r * r <= x:
            r += 1
        return r-1
        