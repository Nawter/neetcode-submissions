class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        n = len(s)
        count = {}
        i = 0

        for j in range(n):
            count[s[j]] = count.get(s[j],0) + 1
            while (j - i + 1) - max(count.values()) > k:
                count[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)

        return res