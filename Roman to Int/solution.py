class Solution:
    def romanToInt(self, s: str) -> int:
        dict_r = {"I":1,
                  "V":5,
                  "X":10,
                  "L":50,
                  "C":100,
                  "D":500,
                  "M":1000}
        count = 0
        list_s = list(s)
        for i,j in enumerate(list_s[:-1]):
            if dict_r[j] < dict_r[list_s[i+1]]:
                count += (dict_r[list_s[i+1]] - dict_r[j])
                count -= dict_r[list_s[i+1]]
                print(count)
            else:
                count += dict_r[j]
                print(count)
        count += dict_r[list_s[-1]]
        return count

        