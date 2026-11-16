class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = {}
        nums.sort()
        
        for num in nums:
            res[num] = res.get(num,0) + 1
        
        arr = []
        for num,count in res.items():
            arr.append([count,num])

        end = []
        arr.sort()
        for i in range(len(arr)):
            if i<k:
                end.append(arr.pop()[1])

        return end
