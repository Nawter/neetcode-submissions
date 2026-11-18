class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for i in range(len(s)):
            if s[i].isalnum():
                res.append(s[i].lower())
        
        i,j= 0, len(res)-1
        while i < j:
            if res[i] != res[j]:
                return False
            i,j=i+1,j-1
        
        return True