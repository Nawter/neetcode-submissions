class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

        # check again because of this
        # if len(s) != len(t):        
        #    return False
        # return sorted(s) == sorted(t)

        