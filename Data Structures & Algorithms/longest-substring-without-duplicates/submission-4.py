class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        n = len(s)
        i = 0
        char_set = set()
        for j in range(n):
            while s[j] in char_set:
                char_set.remove(s[i])
                i +=1

            char_set.add(s[j])

            res = max(res, j - i + 1) 

        return res