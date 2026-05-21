class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        mb=prices[0]
        mp=0
        for p in prices:
            if p<mb:
                mb=p
            else:
                mp=max(mp,p-mb)
        return mp