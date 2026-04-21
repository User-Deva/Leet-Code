class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        return self.climbStairs(n-1)+self.climbStairs(n-2)

        # time limit exceeded for n=45, so we can use dynamic programming to optimize it``