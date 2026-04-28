class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    tmp = tuple([nums[i], nums[l], nums[r]])
                    res.add(tmp)
                    l, r = l + 1, r - 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return [list(t) for t in res]



        