class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            length = 1
            if num - 1 not in nums_set:
                # num is the first number of a run
                # your counting goes here
                while num+length in nums_set:
                    length +=1             
           

            longest = max(longest, length)

        return longest    