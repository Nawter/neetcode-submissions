class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Create map frequency, counter and left pointer
        l = 0
        count = {}
        res = 0 

        # Move right pointer
        for r in range(len(s)):
        # update map frequency of the right
            count[s[r]] = 1 + count.get(s[r],0)
        # update the max frequency with highest frequency
        # if condition violated (<=k) using while (window size - maxf) >k 
        # reduce window size and move left forward
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
        
        # update result with current window size.
            res = max(res, r - l + 1)

        return res