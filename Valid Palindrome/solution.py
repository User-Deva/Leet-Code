class Solution:
    def isPalindrome(self, s: str) -> bool:
        re = "".join([char for char in s if char.isalnum()])
        rev = re[::-1]
        if re.lower() == re[::-1].lower():
            return True
        else:
            return False
      
        