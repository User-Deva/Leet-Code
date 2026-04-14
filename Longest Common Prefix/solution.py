class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        v = sorted(strs)
        f = v[0]
        print(f)
        l = v[-1]
        print(l)
        prefix =''
        # print(sorted(strs))
        for i in range(min(len(l),len(f))):
            if f[i] != l[i]:
                return prefix
            prefix += f[i]
            print(prefix)
        return prefix




class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_c = 2600
        prefix = ''
        for i in strs:
            if min_c > len(i):
                min_c = len(i)
        # first_ele = list(map(lambda x: x[0], strs))
        for i in range(min_c):
            element = list(set(list(map(lambda x: x[i], strs))))
            print(element)
            if len(element) != 1:
                return prefix
            else:
                prefix += element[0]
        return prefix

        

        
        