class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        res = {}
        
        for i in range(n):
            diff = target - nums[i]

            if diff in res:
                return [res[diff],i]

            res[nums[i]] = i
        
        return -1