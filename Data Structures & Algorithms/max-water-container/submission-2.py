class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = []
        maxm = 0 

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                 result.append(min(heights[j],heights[i])*(j - i))

        maxm = max(result)
        return maxm

