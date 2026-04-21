class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        temp=1
        ans=[1]
        for i in range(1, rowIndex+1):
            val= (temp*(rowIndex - i +1))//i
            ans.append(val)
            temp = val
        return ans