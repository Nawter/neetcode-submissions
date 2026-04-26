class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result =  [0] * n
        for i in range(n):
            prd = 1
            for j in range(n):
                if i == j:
                    continue
                prd = prd * nums[j]
            result[i] = prd
        return result

