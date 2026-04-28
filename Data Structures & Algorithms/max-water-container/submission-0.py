class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = []
        maxm = 0 

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                w = j - i
                h = min(heights[j],heights[i])
                a = w * h
                result.append(a)


        maxm = max(result)
        return maxm

