class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # la = len(a) - 1
        # lb = len(b) - 1
        # temp = 0
        # ans = []
        # while la >= 0 or lb >= 0 or temp:
        #     if la >= 0:
        #         temp += int(a[la])
        #         la -= 1
        #     if lb >= 0:
        #         temp += int(b[lb])
        #         lb -= 1
        #     ans.append(str(temp%2))
        #     temp = temp//2
        # return ''.join(ans[::-1])
        ba = int(a, 2)
        bb = int(b, 2)
        ans = ba+bb
        return f"{ans:b}"
    
        